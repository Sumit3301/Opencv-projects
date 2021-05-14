#Thresholding in opencv
import cv2
img=cv2.imread('stewie.jpg')
cv2.imshow('Orignal',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

#Simple thresholding
threshold, thresh=cv2.threshold(gray,15,255,cv2.THRESH_BINARY)
cv2.imshow('Thresolded',thresh)

#Inverse thresh
threshold, threshinverse=cv2.threshold(gray,15,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Thresolded',threshinverse)

#adaptive threshold
adaptive_thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,1)
cv2.imshow('Thresolded',adaptive_thresh)
cv2.waitKey(0)