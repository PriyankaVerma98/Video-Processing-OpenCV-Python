import cv2
import numpy as np


cap = cv2.VideoCapture('electric meter 2.mp4')
# template = cv2.imread('kwh temp 3.png',0)
# w, h = template.shape[::-1]
while(cap.isOpened()):

    _, frame = cap.read()
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # vid_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
#   res = cv2.matchTemplate(vid_gray,template,cv2.TM_CCOEFF_NORMED)
	cv2.imshow('frame',frame)
    k = cv2.waitKey(5) & 0xFF
	if k == 27:
    	break
# threshold = 0.92
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
    # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1) 
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
cv2.destroyAllWindows()
cap.release()