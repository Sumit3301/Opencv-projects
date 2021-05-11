#Transformations of Image
import cv2
import numpy as np
img=cv2.imread('man.jpg')
cv2.imshow('Orignal',img)

#translation
def translation(img,x,y):
    trans_matrix=np.float32([1,0,x],[0,1,y])
    dimensions=(img.shape[1],img.shape[0])
    return cv2.warpAffine(img,trans_matrix,dimensions)


resized_image=cv2.resize(img,(img.shape[1]//5,img.shape[1]//6),interpolation= cv2.INTER_AREA)

#translation
def translation(img,x,y):
    trans_matrix=np.float32([[1,0,x],[0,1,y]])
    dimensions=(resized_image.shape[1],img.shape[0])
    return cv2.warpAffine(resized_image,trans_matrix,dimensions)
# -x --> left
# -y -->up
#  x -->right
#  y -->down
translated = translation(resized_image,100,200)
cv2.imshow('Translated',translated)

#rotation of image
def rotateimg(img,angle,point=None):
    (height,width)= img.shape[:2]

    if(point is None):
        point=(width//2,height//2)
    
    rotmatrix=cv2.getRotationMarix2D(point,angle,1.0)
    dimensions = (width,height)

    return cv2.warpAffine(resized_image,rotmatrix,dimensions)
    
rotated=rotate(resized_image,45)
cv2.imshow('roteted',rotated)s


cv2.waitKey(0)
