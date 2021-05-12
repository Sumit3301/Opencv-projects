#Contour detection
import cv2
img=cv2.imread('man.jpg')
resized_image=cv2.resize(img,(img.shape[1]//5,img.shape[1]//6),interpolation= cv2.INTER_AREA)
cv2.imshow('orignal',resized_image)

gray=cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey Image',gray)
canny=cv2.Canny(resized_image,125,175)
cv2.imshow('Canny',canny)
cv2.waitKey(0)