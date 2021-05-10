#image operations
import cv2
img=cv2.imread('man.jpg')
resized_image=cv2.resize(img,(img.shape[1]//5,img.shape[1]//6),interpolation= cv2.INTER_AREA)
cv2.imshow('orignal',resized_image)
gray=cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image',gray)

#blur image
blur=cv2.GaussianBlur(resized_image,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blur)
#edge cascading/canny edge detection
canny=cv2.Canny(blur,225/3,225)
cv2.imshow('Canny Image',canny)

#dilating image
dilate=cv2.dilate(canny,(5,5),iterations=3)
cv2.imshow('Dilated Image',dilate)

#eroding
erode=cv2.erode(dilate,(3,3),iterations=3)
cv2.imshow('Eroded Image',erode)
#cropping
cropped=img[50:100,100:200]
cv2.imshow('Cropped',cropped)
cv2.waitKey(0)