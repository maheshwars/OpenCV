# Pyramid or pyramid represenattion is a type of multi-scale signal representation
# in which a signal or an image is subject to repeated smoothing and subsampling.

# Gaussian pyramid- repeat filtering and subsampling of image.

import cv2
import numpy as np

img = cv2.imread('lena.jpg')
"""lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr1 = cv2.pyrUp(lr2)"""
layer = img.copy()
gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

cv2.imshow('Original Image', img)
"""cv2.imshow('pyrdown1 Image', lr1)
cv2.imshow('pyrdown2 Image', lr2)
cv2.imshow('pyrup1 Image', hr1)"""
cv2.waitKey(0)
cv2.destroyAllWindows()