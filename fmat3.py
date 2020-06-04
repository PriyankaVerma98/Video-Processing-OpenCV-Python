import cv2
import numpy as np
import os, os.path

# homography with multiple images passed ... edited  

cap = cv2.VideoCapture('1phmetervideo.mp4')

imageDir = "/Users/PV/FOLDERS/PS/tems/"  #specify your path here
image_path_list = []
valid_image_extensions = [ ".png"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]
#create a list all files in directory and
#append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

#loop through image_path_list to open each image
for imagePath in image_path_list:
    print(imagePath) 
    image = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)

    # if image is not None:
    #     cv2.imshow(imagePath, image)
    # elif image is None:
    #     print ("Error loading: " + imagePath)
    #     #end this loop iteration and move on to next image
    #     continue

# img= cv2.imread("A2.png", cv2.IMREAD_GRAYSCALE) # query image

# Features
sift = cv2.xfeatures2d.SIFT_create()
kp_image, desc_image = sift.detectAndCompute(image, None)
#img = cv2.drawKeypoints(img, kp_image, img)

# Feature matching
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

while (cap.isOpened()):
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # trainimage
    
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
    #grayframe = cv2.drawKeypoints(grayframe, kp_grayframe, grayframe)
    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
    
    good_points = []
    for m, n in matches:
        if m.distance < 0.8*n.distance:
            good_points.append(m)

#img3 = cv2.drawMatches(img, kp_image, grayframe, kp_grayframe, good_points, grayframe)

#homography

    if len(good_points) > 3:
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
        
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
 
        # Perspective transform
        h, w = image.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        if matrix is not None:
            dst = cv2.perspectiveTransform(pts, matrix)
            homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 2)
            cv2.imshow("Homography", homography)
    else:
        cv2.imshow("Homographywith3only", grayframe)



#cv2.imshow("Image", img)
#cv2.imshow("grayFrame", grayframe)
# cv2.imshow("img3", img3)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()