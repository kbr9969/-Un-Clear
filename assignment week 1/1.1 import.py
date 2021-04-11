import cv2
import numpy as np


orig = cv2.imread('assignment week 1\\batman.jpg')
orig = cv2.resize(orig, (1280,720))

gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
ret,BW = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('gray',gray)
cv2.imshow('BW',BW)
cv2.waitKey(0)
