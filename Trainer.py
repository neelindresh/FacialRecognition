import cv2
import numpy as np
import os
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("fface.xml")
path='dataset'

def getImageWithID(path):
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
	faces=[]
	ids=[]
	print(imagePaths)
	for imgpth in imagePaths:
		faceImg = Image.open(imgpth).convert('L')
		faceNp = np.array(faceImg, 'uint8')
		Id = int(os.path.split(imgpth)[-1].split(".")[1])
		faces.append(faceNp)
		ids.append(Id)
		cv2.imshow("train", faceNp)
		cv2.waitKey(100)
	return ids,faces

ids,faces=getImageWithID(path)
recognizer.train(faces,np.array(ids))
recognizer.write('recognizer/trainData.yml')
cv2.destroyAllWindows()
