
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('Peter.jpg')

#bgr to gray
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

#bgr to hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)

#bgr to lab
lab=cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
cv2.imshow('LAB',lab)

#hsv to bgr
hsv_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV TO BGR',hsv_bgr)

#bgr to rgb(in open cv it is in the form of bgr whereas without opencv it is rgb)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',rgb)
plt.imshow(rgb)#showing rgb in plot
plt.show()


cv2.waitKey(0)
