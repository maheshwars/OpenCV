"""        Harris Corner Detector
1. Determine which windows produce very large variations in intensity when moved in both X and Y directions.
2. With each window found, a score R is computed.
3. After applying a threshold to this score, important corners are selected & marked.

"""

import cv2
import  numpy as np 

img = cv2.imread('chessboard.png')
cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04) #(img, block_size(size of window),kszie(aperture parameter of Sobel derivative used.)
#                                               ,k- Harris detector free parameter in the equation. )

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] =  [0, 0, 255]

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()