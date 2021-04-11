import cv2
import numpy


cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
     
    cv2.imshow('cam', frame)
    if cv2.waitKey(1) & 0xFF == 27:
            break
cv2.destroyAllWindows()



