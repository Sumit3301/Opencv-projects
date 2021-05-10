#drawing shapes and blank boxes
import cv2
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv2.imshow('blank',blank)

blank[:]=255,255,255

cv2.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv2.FILLED)
cv2.imshow('rectangle',blank)

cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),20,(0,0,255),thickness=-1)
cv2.imshow('circle',blank)

cv2.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=2)
cv2.imshow('line',blank)

cv2.putText(blank,'Hello MY NAME IS SUMIT',(blank.shape[1]//2,blank.shape[0]//2),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,0),4)
cv2.imshow('Text',blank)
cv2.waitKey(0)