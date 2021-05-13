#bitwise operations in openCV
import cv2
from cv2 import data
import numpy as np
blank=np.zeros((400,400),dtype='uint8')

rectangle= cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle=cv2.circle(blank.copy(),(200,200),200,255,-2)

cv2.imshow('Rectangle',rectangle)
cv2.imshow('Circle',circle)

#bitwise and
bitwise_and=cv2.bitwise_and(rectangle,circle)
cv2.imshow('Bitwise and',bitwise_and)

#bitwise or
bitwise_or=cv2.bitwise_or(rectangle,circle)
cv2.imshow('Bitwise OR',bitwise_or)

#bitwise xor
bitwise_xor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow('Bitwise XOR',bitwise_xor)

#bitwise not invert image
bitwise_not=cv2.bitwise_not(rectangle)
cv2.imshow('NOT',bitwise_not)

cv2.waitKey(0)