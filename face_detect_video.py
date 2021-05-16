#face detection using webcam a video
import cv2
import numpy as np


def face_detect(gray,frame):
    haar_cascade=cv2.CascadeClassifier('haar_face.xml')
    faces_ret = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    print(faces_ret)#coordinates of faces
    print(len(faces_ret)) #It will print the number of faces found in the image
    for(x,y,width,height) in faces_ret:
        cv2.rectangle(frame,(x,y),(x+width,y+height ),(0,255,0),1)
    return frame

capture=cv2.VideoCapture(0)
while(True):
    ret,frame=capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detected=face_detect(gray,frame)
    cv2.imshow('Detected',detected)
    if cv2.waitKey(1) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()
