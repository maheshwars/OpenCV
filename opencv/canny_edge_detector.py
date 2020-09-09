#The Canny edge detector is an edge detection operator that uses a multi-stage algorithm
#to detect a wide range of edges. It was developed by John F.Canny in 1986.

"""Composedo of 5 steps:
 1) Noise Reduction
 2) Gradient Calculation
 3) Non-Max Suppression
 4) Double Threshold
 5) Edge Tracking by Hysteresis
 """

import cv2
import numpy as np 
import matplotlib.pyplot as plt 


def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('th1','image', 0, 300, nothing)
cv2.createTrackbar('th2', 'image', 0, 300, nothing)
th1=0
th2=0
img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)

while(1):
    print(th1,th2)
    canny = cv2.Canny(img , th1, th2)
    images = [img, canny]
    titles = ['image', 'Canny']
    th1 = cv2.getTrackbarPos('th1', 'image')
    th2 = cv2.getTrackbarPos('th2', 'image')
    for i in range(len(images)):
        plt.subplot(1,2, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
        print('for')
    plt.show()
    k = cv2.waitKey(1) & 0xFF
    if k == 'b':
        print('break')
        break
    print('while')
    
cv2.destroyAllWindows()
