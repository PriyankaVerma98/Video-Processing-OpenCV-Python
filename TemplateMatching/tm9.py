import cv2

#it captures different frames one by one , by pressing esc button 

cap = cv2.VideoCapture('1ph meter video.mp4')

amount_of_frames = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
# amount_of_frames = cap.get(cv2.CV_CAP_PROP_FRAME_COUNT) for opencv3 

# index = cap.get(CV_CAP_PROP_POS_FRAMES)
# if index % 10 == 0 : 


# print("amount_of_frames",amount_of_frames)
# print("calculated frames",31.4 * 166) = 5212.4 , previously 5180 ! 
# while(cap.isOpened()): 
for index in range(1, int(amount_of_frames)) :
	cap.set(1,index) # Where frame_no is the frame you want => kW frame  !!!!!!!
	index += 1000
	ret, frame = cap.read() # Read the frame
		# if ret == False:
  #   		print("Frame is empty")
	cv2.imshow('window_name', frame) # show frame on window

while True:
	ch = 0xFF & cv2.waitKey(1) # Wait for a second
	if ch == 27:
		break
# from cv2 import __version__
# # 
# print(__version__)