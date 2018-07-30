
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('fface.xml')
# eye_cascade=cv2.CascadeClassifier('eye.xml')
cap = cv2.VideoCapture(0)
# fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x-50, y-100), (x + w+50, y + h+50), (0, 0, 0), 2)


    cv2.imshow('vlo', img)

    if  cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
