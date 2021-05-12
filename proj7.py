#Contour detection
import cv2
img=cv2.imread('man.jpg')
resized_image=cv2.resize(img,(img.shape[1]//5,img.shape[1]//6),interpolation= cv2.INTER_AREA)
cv2.imshow('orignal',resized_image)
blur=cv2.GaussianBlur(resized_image,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blur)
gray=cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey Image',gray)
canny=cv2.Canny(blur,125,175)
cv2.imshow('Canny',canny)

contours,heiarchies = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))
cv2.waitKey(0)