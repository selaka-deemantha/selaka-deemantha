import cv2
import numpy as np
img=cv2.imread('download.jpg')

#join images horizontaly

imghor=np.hstack((img,img))

#join images verticaly

imgver=np.vstack((img,img))


cv2.imshow('horizontal',imghor)
cv2.imshow('vertical',imgver)
cv2.waitKey(0)