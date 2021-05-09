#resize/rescale video in opencv
import cv2

def rescaleframe(frame,scale=0.4):
    width=int(frame.shape[0]*scale)
    height=int(frame.shape[1]*scale)
    return cv2.resize(frame,[width,height],interpolation=cv2.INTER_AREA)

capture=cv2.VideoCapture(0)

while(True):
    ret,frame=capture.read()
    resized_frame=rescaleframe(frame)
    cv2.imshow('resized',resized_frame)
    if cv2.waitKey(1) & 0xFF==ord('d'):
        break

cv2.waitKey(0)