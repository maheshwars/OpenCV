#morphological transformers are some simple operations based on image shapes.
#normally performed on binary images.
#two things required. 1) Original image
#   2)kernel - A kernel tells you how to change the value of any given pixel by combining it with different
# amounts of the neighboring pixels.
              
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)       # increase the size to cover more area and make the balls bigger
dilation = cv2.dilate(mask, kernal, iterations = 2) #to reduce the size of black inside the white balls. it=2 for more dilation
erosion = cv2.erode(mask,  kernal, iterations = 1)# errodes the outer layers of balls making it smaller.
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # opening = erosion -> dilation.
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal)  # closing = dialtion -> erosion.
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)   # mg= dilation - erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)     # th = image - opening

titles = ['image','mask','dilation','erosion','opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2,4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

 




