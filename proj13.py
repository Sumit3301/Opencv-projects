#Computing histogram
import cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import blackman
img=cv2.imread('peter.jpg')
#cv2.imshow('Orignal',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)
blank=np.zeros(img.shape[:2],dtype='uint8' )
#grayscale histogram
gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# Of piels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)