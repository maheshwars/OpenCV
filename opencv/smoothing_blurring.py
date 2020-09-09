#smoothing removes noise in the images.
# use linear filters like: homogeneous filters, Gaussion filter, Medain filter, Bilateral filter

# In image processing, a kernel, a convolutional matrix, or mask is a small matrix. It is used for blurring,
#sharpening, embossing, edge detection, and more.

#homogeneous filter is simplest, each output pixel is the mean of its kernel neighbors.

#Gaussian filter is nothing but using different-weighted-kernel, in both x and y direction.
#pixel on center have higher weight than on the outer matrix of the kernel

#Median filter replaces each pixel's value with the median of its neighboring pixels. Great in dealing with Salt and pepper noise.

#Bilateral filter preserves Edges in the  image.

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # matplotlib reads in rgb format.

kernel = np.ones((5,5), np.float32)/25
# as in 1D signals, images can also be filtered with Low Pass Filters(LPF), High Pass Filters(HPF),etc.
# LPF removes noises, blurrinf the images.
# HPF helps finding edges in the images.
dst = cv2.filter2D(img ,-1, kernel)          # arg2 - depth
blur = cv2.blur(img, (5,5))                  # blur also called averaging
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)              # arg2- kernel size # salt_pepper for median
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # arg2- diameter of pixel neighbor in filter,3- sigma color,4- sigma space

titles =['image','2D convolution', 'blur', 'GasussianBlur','MedianBlur','bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(3,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

