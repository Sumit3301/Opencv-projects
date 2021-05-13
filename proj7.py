#Contour detection
import cv2
import numpy as np
img=cv2.imread('peter.jpg')

resized_image=cv2.resize(img,(img.shape[1]//5,img.shape[1]//6),interpolation= cv2.INTER_AREA)
#cv2.imshow('orignal',resized_image)

blank=np.zeros(img.shape,dtype='uint8')


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey Image',gray)
blur=cv2.GaussianBlur(gray,(1,1),cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blur)

ret,thresh = cv2.threshold(blur,125,255,cv2.THRESH_BINARY)

#canny=cv2.Canny(blur,125,175)

contours,heiarchies = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Thresh',thresh)
print(len(contours))

cv2.drawContours(blank,contours,-1,(0,0,255),2)
cv2.imshow('Contours',blank)
cv2.waitKey(0)