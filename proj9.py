#color channels in opencv
import cv2
import numpy as np

img=cv2.imread('peter.jpg')
cv2.imshow('Orignal',img)
blank=np.zeros(img.shape[:2],dtype='uint8')#creating blank image using numpy
b,g,r=cv2.split(img)#splitting the bgr channels of the image
blue=cv2.merge([b,blank,blank])
green=cv2.merge([blank,g,blank])
red=cv2.merge([blank,blank,r])
#displaying the various channels of the image
cv2.imshow('Blue',blue)
cv2.imshow('Green',green)
cv2.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
merge=cv2.merge([b,g,r])
cv2.imshow('Merge',merge)
cv2.waitKey(0)