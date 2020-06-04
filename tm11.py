import numpy as np
import cv2

# works fine 

cap = cv2.VideoCapture('1ph meter video.mp4') #video_name is the video being called
amount_of_frames = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

# for frame_no in range(int(amount_of_frames)) :

frame_no = 518
cap.set(1,frame_no); # Where frame_no is the frame you want
ret, frame = cap.read() # Read the frame
cv2.imshow('window_name', frame) # show frame on wind

while True:
    ch = 0xFF & cv2.waitKey(1) # Wait for a second
    if ch == 27:
        break