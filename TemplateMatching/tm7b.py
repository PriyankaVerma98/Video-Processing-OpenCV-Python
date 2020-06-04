import cv2
import numpy as np
 

cap= cap = cv2.VideoCapture('1ph meter video.mp4')
 
while True:
    ret, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
 
    lower_green = np.array([50, 155, 155])
    upper_green = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
 
contours, hierarchy  = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
    #for contour in contours:
        #area = cv2.contourArea(contour)
 
       # if area > 5000:
    #cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
    
    
    #find the biggest area
c = max(contours, key = cv2.contourArea)

x,y,w,h = cv2.boundingRect(c)
    # draw the reading area contour (in blue)
im=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
roi=im[y:y+h,x:x+w]
    
    
cv2.imshow("Frame", frame)
# cv2.imshow("Mask", mask)
cv2.imshow("Result",roi)

key = cv2.waitKey(1)
if key == 27:
   break
 
cap.release()
cv2.destroyAllWindows()