#Maksing in openCV
import cv2
import numpy as np
img=cv2.imread('peter.jpg')
cv2.imshow('Orignal',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('Blank',blank)
mask=cv2.circle(blank,(img.shape[1]//2+30,img.shape[0]//2),300,255,-1)
cv2.imshow('Mask before',mask)
masked=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked After',masked)
cv2.waitKey(0)

