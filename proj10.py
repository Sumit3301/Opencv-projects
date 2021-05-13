#blurring of images to remove noise from the image
import cv2

img=cv2.imread('peter.jpg')
cv2.imshow('Orignal',img)

#averaging of pixels for the middle value of the kernel
avg=cv2.blur(img,(7,7))
cv2.imshow('Average',avg)

#gaussian blur
gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian Blur',gaussian)

#median blur
median=cv2.medianBlur(img,7)
cv2.imshow('Median Blur',median)

#Biateral Blur
bilateral=cv2.bilateralFilter(img,5,15,15)
cv2.imshow('Bilateral Blur',bilateral)
cv2.waitKey(0)