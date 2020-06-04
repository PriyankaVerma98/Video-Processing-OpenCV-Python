import cv2
import numpy as np
import time 

# only the feature matching  not homography + included function in it   !!! 
# kw h ---  works 
# AP --- works 
# k  
# volt not works 

cap = cv2.VideoCapture('1phmetervideo.mp4')
img = cv2.imread("1kwh temp 2.png", cv2.IMREAD_GRAYSCALE)
img2= cv2.imread("2kwtemp2.png", cv2.IMREAD_GRAYSCALE)
img3= cv2.imread("4A2.png", cv2.IMREAD_GRAYSCALE)
img4= cv2.imread("2kwtemp2.png", cv2.IMREAD_GRAYSCALE)

def function_bla(img,vid_gryframe): 

    sift = cv2.xfeatures2d.SIFT_create()
    kp_image, desc_image = sift.detectAndCompute(img, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    kp_grayframe, desc_grayframe = sift.detectAndCompute(vid_gryframe, None)

    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
    
    good_points = []
    for m, n in matches:
        if m.distance < 0.8*n.distance:
            good_points.append(m)
    # time.sleep(1)
    video = cv2.drawMatches(img, kp_image, vid_gryframe, kp_grayframe, good_points, vid_gryframe)

    if len(good_points) > 4 :
        return video
    
    else :
        return (0)



# def video_to_frames(video, path_output_dir):
#     # extract frames from a video and save to directory as 'x.png' where
#     # x is the frame index
#     vidcap = cv2.VideoCapture(video)
#     count = 0
#     while vidcap.isOpened():
#         time.sleep(1)
#         success, image = vidcap.read()
#         if success:
#             cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
#             count += 1
#         else:
#             break
#     cv2.destroyAllWindows()
#     vidcap.release()
# video_to_frames('C:/Users/Win10/Documents/4th Semester Summer/GUVNL/3 ph.mp4', 'F:/3 ph')

while(cap.isOpened()):
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("video",grayframe)
    # cv2.imshow("video",frame)
    # time.sleep(1)
    return1= function_bla(img,grayframe)
    if return1 is not None :
        cv2.imshow("video",return1)
    else :
        return2 = function_bla(img2,grayframe)
        if return2 is not None:
            cv2.imshow("video",return2)
        else :
            return3 = function_bla(img3,grayframe) 
            if return3 is not None :
                cv2.imshow("video",return3)
            else : 
                cv2.imshow("video",grayframe)

    key = cv2.waitKey(0)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()