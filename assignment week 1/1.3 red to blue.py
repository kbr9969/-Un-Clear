import cv2
import numpy as np

img = cv2.imread('assignment week 1/Thor.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lred = np.array([0,70,20])
ured = np.array([18,255,255])

lred2 = np.array([162,70,20])
ured2 = np.array([180,255,255])

mask = cv2.inRange(hsv, lred, ured)
maskf = cv2.inRange(hsv, lred2, ured2)
maskf = mask + maskf
mask_inv = cv2.bitwise_not(maskf)

add1 = cv2.bitwise_and(img, img, mask = maskf)
add1 = cv2.cvtColor(add1, cv2.COLOR_BGR2RGB)
add2 = cv2.bitwise_and(img, img, mask = mask_inv)

final = cv2.add(add1,add2)
cv2.imshow('thor',img)
#cv2.imshow('mask', mask)
#cv2.imshow('add2', add2)
cv2.imshow('blue thor',final)
cv2.waitKey(0)
cv2.destroyAllWindows()