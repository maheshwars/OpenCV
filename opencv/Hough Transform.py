# Hough Transform
"""The Hough transform is a popular technique to detect any shape,
    if can represent that shape in a mathematical form. It can detect
    the shape even if it is broken or distorted a little bit.

A line in the image space can be expressed with two variables. ex-
- In Cartesioan Coordinate system yi = mxi + c.
- In Polar Coordinate system x cos0 + y sin0 = r

Hough transformation algo- 
1. edge detection eg. using the canny edge detector.
2. mapping of edge points to the Hough sapce and storage in an accumulator.
3. interpretation of the accumulator tp yield lines of infinite length.
    The interpretation is done by thresholding and possibly other constants.
4. Conversion of infinite lines to finite lines. 

OpenCV implements two kinds of Hough Line Transforms
- The Standard Hough Transform(Hoough lines method)
- The Probabilistic Hough Line Transform(HoughLinesP Method)
"""
import cv2
import numpy as np 

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
#args2 - lines: Output vector of lines. Each lines is represented by a 2 or 3 element vector (rho,theta) 
#        or (rho,theta,votes).rho is the distance from the coordinate origin(0,0) (top-left corner). theta
#        is the line rotation angles in radians. vote is the value of accumulator
#args3 - rho: disrance resolutions of the accmulator in the pixels.
#args4 - theta: Angle resolution of the accumulator in radians.
#args5 - threshold: Accumulator threshold parameter. Only those lines are returned that get enough votes(>threshold).
  
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    #x1 stores the rounded off value of (r*cos0 - 1000*sin0)
    x1 = int(x0 + 1000 * (-b))
    #y1 stores the rounded off value of (r*sin0 + 1000*cos0)
    y1 = int(y0 + 1000 * (a))
    #x2 stores the rounded off value of (r*cos0 + 1000*sin0)
    x2 = int(x0 - 1000 * (-b))
    #y2 stores the rounded off value of (r*sin0 - 1000*cos0)
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 2)
cv2.imshow("canny", edges)
cv2.imshow("Hough lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()