import cv2
import numpy as np

# homography 

#Results : kW not works on video 1 even with 3, nor new template 
# kWh works with 5
# ampere  proper  with 5... works with 4 too 
# kw works in 2nd round with 4 .... check with new temp 

cap = cv2.VideoCapture('1phmetervideo.mp4')
img= cv2.imread("kwh better.png", cv2.IMREAD_GRAYSCALE) # query image

# Features
sift = cv2.xfeatures2d.SIFT_create()
kp_image, desc_image = sift.detectAndCompute(img, None)
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
    
    if len(good_points) > 4:
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
        
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
 
        # Perspective transform
        h, w = img.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)
 
        homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 2)
 
        cv2.imshow("Homography", homography)
    else:
        cv2.imshow("Homography", grayframe)
 
    
    
    #cv2.imshow("Image", img)
    #cv2.imshow("grayFrame", grayframe)
    # cv2.imshow("img3", img3)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()