
import cv2
import numpy as nm
import urllib.request

face_cascade = cv2.CascadeClassifier('fface.xml')
# eye_cascade=cv2.CascadeClassifier('eye.xml')
#cap = cv2.VideoCapture(0)
# fgbg=cv2.createBackgroundSubtractorMOG2()
url="http://192.168.43.100:8080/shot.jpg"
while True:
    imgRes = urllib.request.urlopen(url)
    imgn = nm.array(bytearray(imgRes.read()), dtype=nm.uint8)
    img = cv2.imdecode(imgn, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x-50, y-100), (x + w+50, y + h+50), (0, 0, 0), 2)


    cv2.imshow('vlo', img)

    if  cv2.waitKey(10)==ord('q'):
        break


cv2.destroyAllWindows()
