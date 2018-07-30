import numpy as nm
import cv2
import urllib.request

url="http://192.168.43.100:8080/shot.jpg"
while True:
    imgRes=urllib.request.urlopen(url)
    img=nm.array(bytearray(imgRes.read()),dtype=nm.uint8)
    imgn=cv2.imdecode(img,-1)
    cv2.imshow('test',imgn)
    cv2.waitKey(10)