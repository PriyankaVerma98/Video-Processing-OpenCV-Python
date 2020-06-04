import cv2
import numpy as np
import glob  
import imutils 

#kwh 
# detects kW for V template @ .85 and @.9
#runs slow at .91 onwards , detects only V frame : ask mayur to check 
cap = cv2.VideoCapture('1phmetervideo.mp4')
template = cv2.imread("3vtemp2.png",0)
w, h = template.shape[::-1]

# for scale in np.linspace(.35, 1, 5)[::-1]:
resized = imutils.resize(template, width = int(template.shape[1] * .35))
r = template.shape[1] / float(resized.shape[1])

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray,resized,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85

    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
    	cv2.rectangle(frame, pt, (pt[0] + int(w*0.35), pt[1] + int(h*0.35)), (0,255,255), 1) 
 	cv2.imshow('frame',frame)
	cv2.imshow('resized',resized)
	cv2.imshow('template',template)
	
    k = cv2.waitKey(1) & 0xFF       
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
