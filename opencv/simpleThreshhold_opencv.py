import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("gradient.png",0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # threshold(img , thrshold, max, thrshold type)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # inverse
_, th3 = cv2.threshold(img, 180, 255, cv2.THRESH_TRUNC) # upto 180 the pixel value will not change
_, th4 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO) #pixel<127 will be 0. Inverse- cv2.THRESH_TOZERO_INV

#using matplotlib
titles = ['ORIGINAL_IMAGE','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO']
images = [img, th1, th2, th3, th4]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray') #  gray for no color
    plt.xticks([]),plt.yticks([])
#using cv2
"""cv2.imshow("image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)"""
plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()