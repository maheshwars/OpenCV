# Pyramid or pyramid represenattion is a type of multi-scale signal representation
# in which a signal or an image is subject to repeated smoothing and subsampling.

# Gaussian pyramid- repeat filtering and subsampling of image.

# Laplasion Pyramid - A level in Laplasian Pyramid is formed by the difference b/w
# that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.

import cv2
import numpy as np

img = cv2.imread('lena.jpg')

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)
    
for i in range(5,0,-1):
    Gauss_extended = cv2.pyrUp(gp[i])
    Laplacian = cv2.subtract(gp[i-1], Gauss_extended)
    cv2.imshow(str(i), Laplacian)

cv2.imshow('Original Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()