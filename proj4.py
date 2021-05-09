#drawing shapes
import cv2
import numpy as np
blank=np.zeros((200,200,3),dtype='uint8')
cv2.imshow('blank',blank)

blank[:]=255,255,255
cv2.imshow('green',blank)

cv2.waitKey(0)