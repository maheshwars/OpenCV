import cv2
import numpy as np 

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize= 3)
cv2.imshow("edges_canny", edges)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap= 10)
#args1 - lines: Output vector of lines. Each lines is represented by a 2 or 3 element vector (rho,theta) 
#        or (rho,theta,votes).rho is the distance from the coordinate origin(0,0) (top-left corner). theta
#        is the line rotation angles in radians. vote is the value of accumulator
#args2 - rho: disrance resolutions of the accmulator in the pixels.
#args3 - theta: Angle resolution of the accumulator in radians.
#args4 - threshold: Accumulator threshold parameter. Only those lines are returned that get enough votes(>threshold).
#args5 - minLineLength: Minimum length of line segments shorter than this are rejected.
#args6 - mxLineGap: Maximum allowed length of line segments to treat them as single line.

for line in lines:
    x1, y1, x2 ,y2 = line[0]
    lines = cv2.line(img,(x1, y1), (x2,y2), (0,255,0), 2)

cv2.imshow("prob_hough_lines", img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()