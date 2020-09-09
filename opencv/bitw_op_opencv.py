import cv2
import numpy as np 

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1 , (200,0), (300,100), (255,255,255),-1)
img2 = cv2.imread('image_1.png')

#resize both images to same size
img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2 , (512,512))

#bitAnd = cv2.bitwise_and(img2,img1)
#bitOr = cv2.bitwise_or(img2,img1)
#bitXor = cv2.bitwise_xor(img2, img1)
bit_Not1 = cv2.bitwise_not(img1)
bit_Not2 = cv2.bitwise_not(img2)

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
#cv2.imshow("bitwAnd",bitAnd)
#cv2.imshow("bitwOR",bitOr)
#cv2.imshow("bitwXor",bitXor)
cv2.imshow("bitwNot1",bit_Not1)
cv2.imshow("bitwNot2",bit_Not2)

cv2.waitKey(0)
cv2.destroyAllWindows()

