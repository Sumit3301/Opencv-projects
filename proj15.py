#Gradiant and edge detetion in OpenCV
import cv2
import numpy as np

img=cv2.imread('stewie.jpg')
cv2.imshow('Orignal',img)

#Conversion to gray color
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray)

#Laplacian method
lap=cv2.Laplacian(gray,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow('Laplacian',lap)

cv2.waitKey(0)