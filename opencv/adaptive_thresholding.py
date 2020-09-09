import cv2 
import numpy as np 

img = cv2.imread("sudoku.png",0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # threshold(img , thrshold, max, thrshold type)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#(arg3- how threshold value is collected
#agr4- threshold type arg5- blocksize(neighbourhood size, agrs), agrs6- constant _C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()