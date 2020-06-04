import cv2
import numpy as np 
import glob  
import imutils

cap = cv2.VideoCapture('1ph meter video.mp4')
template = cv2.imread('kw temp2.png',0)
w, h = template.shape[::-1]
                            
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    
    loc = np.where( res >= threshold)
    
    for pt in zip(*loc[::-1]):
    	cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1) 
    cv2.imshow('frames',frame)
    cv2.imshow('temp',template)
	# cv2.waitKey(0)
    # if cv2.waitKey(5) & 0xFF == ord('q'):       // doesn't exit with escape key
        # break  // 
    k = cv2.waitKey(1) & 0xFF       
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()