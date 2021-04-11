import cv2
import numpy as np


orig = cv2.imread('assignment week 1\\batman.jpg')
orig = cv2.resize(orig, (1280,720))
BW = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(BW,11,150,150)

image = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)



sketch = cv2.bitwise_and(orig, image)
#sketch = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)

cv2.imshow('original',orig)
cv2.imshow('pencil', sketch)
cv2.waitKey(0)