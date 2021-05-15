#Face detection using openCV
import cv2
import numpy as np

img=cv2.imread('faces.jpg')
cv2.imshow('Orignal',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray)

haar_cascade=cv2.CascadeClassifier('haar_face.xml')
faces_ret = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(faces_ret)
print(len(faces_ret)) #It will print the number of faces found in the image

for(x,y,width,height) in faces_ret:
    cv2.rectangle(img,(x,y),(x+width,y+height ),(0,255,0),1)
cv2.imshow('Faces',img )
cv2.waitKey(0)