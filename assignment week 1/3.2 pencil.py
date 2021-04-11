import cv2
import numpy as np


def nothing():
    pass

cv2.namedWindow('controls')
cv2.createTrackbar('t1', 'controls', 0, 256, nothing)
cv2.createTrackbar('t2', 'controls', 0, 256, nothing)


cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    t1 = cv2.getTrackbarPos('t1', 'controls')
    t2 = cv2.getTrackbarPos('t2', 'controls')
    
    ret, frame = cap.read()
    if ret==True:       
        BW = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        filtered = cv2.bilateralFilter(BW,11,150,150)
        filtered = cv2.medianBlur(filtered, 3)
        image = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        sketch = cv2.bitwise_and(frame, image)
        sketch = cv2.resize(sketch, (1280, 720))
        #sketch = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)

        cv2.imshow('cool', sketch)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()