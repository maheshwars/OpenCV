import numpy as np 
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)
"""['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY',
 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
  'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']"""

def click_event(event, x, y, falgs, param):

    if event == cv2.EVENT_LBUTTONDOWN :  
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x,y), 3, (0,0,255),-1)
        color_img = np.zeros([512,512,3], np.uint8) 
        color_img[:] = [blue, green, red] 
        cv2.imshow('newimage', color_img)

    """if event == cv2.EVENT_RBUTTONDOWN :
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img, strBGR, (x,y), font, .5, (0,255,255), 2)
        cv2.imshow('image', img)"""
    
        
#img = np.zeros([512,512,3], np.uint8) 
img =cv2.imread('lena.jpg')   
cv2.imshow('image',img)  
points= []  

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()