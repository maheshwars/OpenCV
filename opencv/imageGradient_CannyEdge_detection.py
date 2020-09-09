# image gradient is a directional change in the intensity or color in an image.

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img , cv2.CV_64F, ksize= 3)                #args2- datatype(64bit float), 
lap = np.uint8(np.absolute(lap))                               # convert to 8bit int
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)                      # arg3- dx, arg4- dy
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)                      # arg3- dx, arg4- dy
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelCombined = cv2.bitwise_or(sobelx, sobely)
edges = cv2.Canny(img , 100, 200)

titles = ['images','Laplacian', 'sobelx', 'sobely', 'sobelCombined','Canny']
images = [img, lap, sobelx, sobely, sobelCombined,edges]

for i in range(len(images)):
    plt.subplot(3,2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()