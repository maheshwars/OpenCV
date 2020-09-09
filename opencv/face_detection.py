"""
First a classifier (namely a cascade of boosted classifiers working with harr-like features)
is trained with a few hundred sample views of a particular object(i.e, a face or a car),
called positive examples, thata are scaled to the same size(say, 20x20), and a negative
examples- arbitrary images of the same size.
"""
import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#img = cv2.imread('messi5.jpg')
cap = cv2.VideoCapture('jetblackheart.mp4')

while(cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            center_coordinates = (ex+(ew//2), ey+(eh//2)) 
            axesLength = (ew//2,eh//3) 
            angle = 0
            startAngle = 0
            endAngle = 360
            color = (0, 255, 0) 
            thickness = 2
            cv2.ellipse(roi_color, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness) 
    cv2.imshow('output', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()   
cv2.destroyAllWindows()