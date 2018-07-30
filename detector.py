import cv2
import numpy as np
import pymysql
def getDetails(id):
    conn = pymysql.connect(host='localhost', user='root', password='', db='face')

    cur = conn.cursor()
    sql = 'select * from userinfo where id=%s;'
    cur.execute(sql,id)
    data = cur.fetchall()
    profile=None
    #print(data)
    for val in data:
        if val is not None:
            profile=val
    return profile

face_cascade = cv2.CascadeClassifier('fface.xml')
# eye_cascade=cv2.CascadeClassifier('eye.xml')
cap = cv2.VideoCapture(0)
# fgbg=cv2.createBackgroundSubtractorMOG2()
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('recognizer/trainData.yml')
id=0
font=cv2.FONT_ITALIC
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        print(id,conf)
        val=getDetails(id)

        #print(val)
        if val is None or conf<40:
            id = 'unknown'
            cv2.putText(img, str(id), (x - 30, y - 30), font, 2, 255)
        else:

            name = val[1]
            cv2.putText(img, 'Name:  ' + str(name), (x, y - 90), font, 1, 255)
            gender = val[2]
            cv2.putText(img, 'Gender:  ' + str(gender), (x, y - 60), font, 1, 255)
            acco = val[3]
            cv2.putText(img, 'Association:  ' + str(acco), (x, y - 30), font, 1, 255)
    cv2.imshow('vlo', img)

    if  cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
