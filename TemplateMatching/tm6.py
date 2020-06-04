import cv2
import numpy as np
import glob  
import imutils

# Read the main image
img_rgb = cv2.imread('kwh i3.jpg')
  
# Convert to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Read the templatex
template = cv2.imread('kw temp2.png',0)
  
# Store width and heigth of template in w and h
w, h = template.shape[::-1]
found = None

for scale in np.linspace(.3, 1, 5)[::-1]:
 
    # resize the image according to the scale, and keep track
    # of the ratio of the resizing
    resized = imutils.resize(template, width = int(template.shape[1] * scale))
    r = template.shape[1] / float(resized.shape[1])
    cv2.imshow('resized',resized)
    # if the resized image is smaller than the template, then break
    # from the loop
    # detect edges in the resized, grayscale image and apply template 
    # matching to find the template in the image 
    edged = cv2.Canny(img_gray, 50, 200) 
    result = cv2.matchTemplate(template,img_gray, cv2.TM_CCOEFF)
    threshold = 0.85
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
    # if we have found a new maximum correlation value, then update
    # the found variable if found is None or maxVal > found[0]:
    # if resized.shape[0] < h or resized.shape[1] < w:
        # break
    found = (maxVal, maxLoc, r)
 #                                                                    //no threshold value ? ? 
# unpack the found varaible and compute the (x, y) coordinates
# of the bounding box based on the resized ratio
(_, maxLoc, r) = found
(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
(endX, endY) = (int((maxLoc[0] + w) * r), int((maxLoc[1] + h) * r))
 
# draw a bounding box around the detected result and display the image
cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 255), 2)
cv2.imshow('img_rgb',img_rgb)
cv2.imshow('template',template)
cv2.waitKey(0)