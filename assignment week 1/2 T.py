import cv2
import numpy as np
#keep closing 10 times to stop this program
T = cv2.imread('assignment week 1/T.PNG')
rows,cols,channels = T.shape

m = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

m = np.float32([[1,0,100],[0,1,-50]])
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

m = np.float32([[1,0,-100],[0,1,-50]])
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

m = np.float32([[1,0,-100],[0,1,50]])
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

m = cv2.getRotationMatrix2D((cols/2,rows/2), 90, 1)
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

m = cv2.getRotationMatrix2D((cols/2,rows/2), 180, 1)
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

m = cv2.getRotationMatrix2D((cols/2,rows/2), 270, 1)
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

m = cv2.getRotationMatrix2D((cols/2,rows/2), 315, 1)
dst = cv2.warpAffine(T,m,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)

dst = cv2.medianBlur(T, 11)
cv2.imshow('img',dst)

dst = cv2.GaussianBlur(T, (9,9), 0)
cv2.imshow('gauss', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()