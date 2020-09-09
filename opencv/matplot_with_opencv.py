import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # convert to RBG to obtain the same image as from cv
plt.imshow(img)
plt.xticks([]), plt.yticks([])                  # to remove x-y axis in plt
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()