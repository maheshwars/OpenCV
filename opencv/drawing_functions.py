import numpy as np
import cv2


#img = cv2.imread('lena.jpg',1)                                             #image from file
img = np.zeros([512,512,3], dtype= np.uint8)                                #for a black image, zeros([height,width,3],dtype)


img = cv2.line(img, (0,0), (300,350), (255,200,0) , 5)                        # draw a line (img,start[cordinates],end[cor],color(BGR),thickness)
img = cv2.arrowedLine(img, (0,0), (100,350), (255,0,400) , 5)
img = cv2.rectangle(img, (100,0), (300,350), (0,255,0) , 2, cv2.LINE_4)                # rectangle(img,p1,p2,color,thickness,linetype) 
                                                                                # thickness = -1 fills the rect. with color
img = cv2.circle(img, (200,200), 50, (0,0,255), -1)                       #circle(img, centre, radius, color,thickness) 

font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img , "lena...", (10,100), font, 2, (0,255,255), 5, cv2.LINE_AA) #putText(img, 'text', start, font_style, font_size, color,
                                                                                        # thickness, line_type)
                                                                                        

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()