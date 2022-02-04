import cv2
import numpy as np
""""
----------->(+x)
|
|
|
|
|
|
\/(+y)
"""
img=cv2.imread('OIP.jpg')
print(img.shape)
#resizing
resizeimg=cv2.resize(img,(300,200))
print(resizeimg.shape)

#cropping
#first height and second width
imgcroped=img[100:200,100:200]


cv2.imshow('img',img)
cv2.imshow('resize',resizeimg)
cv2.imshow('cropped',imgcroped)
cv2.waitKey(0)