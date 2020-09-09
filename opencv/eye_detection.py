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
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0),3)

    cv2.imshow('output', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()   
cv2.destroyAllWindows()