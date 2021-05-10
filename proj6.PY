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




cv2.waitKey(0)
