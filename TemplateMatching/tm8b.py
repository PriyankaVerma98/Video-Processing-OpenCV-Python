import glob

images = [cv2.imread(file) for file in glob.glob("/Users/PV/FOLDERS/PS/tems/*.png")]

for image in images:
    print(imagePath) 
    # image = cv2.imread(imagePath)
    
    # # display the image on screen with imshow()
    # # after checking that it loaded
    # if image is not None:
    #     cv2.imshow(imagePath, image)
    # elif image is None:
    #     print ("Error loading: " + imagePath)
    #     #end this loop iteration and move on to next image
    #     continue