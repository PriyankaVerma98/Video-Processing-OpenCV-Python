import cv2
import numpy as np
import glob  
import imutils 

#kwh 
# detects kW for V template @ .85 and @.9

# not resizing the volt template : detects kW even at .9
# fr 0.92 detects volt properly ..little bit of kW too etected ..needs for pre- processing 

cap = cv2.VideoCapture('1ph meter video.mp4')
template = cv2.imread("v temp4.png",0)
w, h = template.shape[::-1]

# for scale in np.linspace(.35, 1, 5)[::-1]:
# resized = imutils.resize(template, width = int(template.shape[1] * .35))
# r = template.shape[1] / float(resized.shape[1])

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.92

    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
    	cv2.rectangle(frame, pt, (pt[0] + int(w), pt[1] + int(h)), (0,255,255), 1) 
 	cv2.imshow('frame',frame)
	# cv2.imshow('resized',resized)
	cv2.imshow('template',template)
	
    k = cv2.waitKey(1) & 0xFF       
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
