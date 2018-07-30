
import cv2
import pymysql
import numpy as np

def insertData(id):
    conn = pymysql.connect(host='localhost', user='root', password='', db='face')
    print("Hey here is a new Face!!!! Tell be About you:")
    print('Enter Name:')
    name=input()
    print('Enter Gender M/F:')
    gender=input()
    print('Enter association with the admin:')
    assoc=input()
    cur = conn.cursor()
    sql = 'insert into userinfo values(%s,%s,%s,%s);'
    cur.execute(sql,(id,name,gender,assoc))
    conn.commit()


face_cascade = cv2.CascadeClassifier('fface.xml')
cap = cv2.VideoCapture(0)
id=input("enter user id")

sample=0
val=None
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        val=cv2.imwrite("./dataset/user." + id + "." + str(sample) + ".jpg", gray[y:y + h, x:x + w])
        sample += 1
        cv2.waitKey(100)

    cv2.imshow('vlo', img)
    if sample >100:
        break

if val is True:
    insertData(id)
cap.release()
cv2.destroyAllWindows()
