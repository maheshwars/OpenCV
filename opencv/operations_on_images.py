import cv2
import numpy as np 

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape)        #(rows, cols, channels)
print(img.size)         #total number of pixels.
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]            # ROI - Region of interest
img[272:332, 100:160] = ball            # size of ball and img[size] should be same, in this case [60,60,3]

#resize both images to same size
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2 , (512,512))

#dst = cv2.add(img, img2)                               #just adds 
dst = cv2.addWeighted(img, 0.8, img2, 0.2, 0)           # adds with weight

cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
