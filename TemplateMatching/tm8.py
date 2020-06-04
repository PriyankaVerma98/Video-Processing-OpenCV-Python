import cv2
import numpy as np
import glob  
import imutils 

cap = cv2.VideoCapture('1ph meter video.mp4')

fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)     # value of fps 
# cap.set(cv2.cv.CV_CAP_PROP_FPS, 15)
print "Frames per second using cap.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)



#make a list of all template images from a directory
# X_data = []
# files1= glob.glob('*.png')
# for myfile in files1:
#     template = cv2.imread(myfile,0)
#     X_data.append (template)
    
#  kW gives good result 

template = cv2.imread('kw temp2.png',0)
w, h = template.shape[::-1]

resized = imutils.resize(template, width = int(template.shape[1] * .35))
r = template.shape[1] / float(resized.shape[1])

while(cap.isOpened()):
    index = cap.get(cv2.CAP_PROP_POS_FRAMES)   # this function gives error 
    
    # if index % 5 == 0:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray,resized,cv2.TM_CCOEFF_NORMED)
    threshold = 0.92

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
