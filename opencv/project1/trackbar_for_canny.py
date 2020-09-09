import cv2
import numpy as np 

def nothing(x):
    pass

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,)* channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

image = cv2.imread('road1.jpg')
cv2.namedWindow("image")

cv2.createTrackbar("th1", "image",0,300, nothing)
cv2.createTrackbar("th2", "image", 0, 300, nothing)

height = image.shape[0]
width = image.shape[1]

ROI_verties = [
    (0,height),
    (width/2 +  100, height/2 + 200),
    (width, height)

]
cropped_image = region_of_interest(image, np.array([ROI_verties], np.int32))
gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)



while(1):
    th1 = cv2.getTrackbarPos('th1','image')
    th2 = cv2.getTrackbarPos('th2','image')
    canny = cv2.Canny(gray_image, th1, th2)
    cv2.imshow('image',canny)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    
cv2.destroyAllWindows()

