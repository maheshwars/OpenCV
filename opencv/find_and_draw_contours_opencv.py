#contors is a Python list of all the contours in the image. Each infividual contors
# is a numpy array of (x,y) cooordinates of boundary points of the object.


import cv2
import numpy as np 

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
ret , thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # finds contours
print('Number of contors = ' + str(len(contours)))

cv2.drawContours(img, contours, -1, (0,255,0),3) #(draws contours on the image, agrs3- nth contour((0-8), for this case) or -1 for all contours
                                                  # args4- color, args5- thickness)                      
cv2.imshow('image', img)
cv2.imshow('image gray', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()