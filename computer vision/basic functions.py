import cv2
import numpy as np
img=cv2.imread('OIP.jpg')

#gray image
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur image
#--important--
#kernal should contain odd numbers like 3,7,9,1
imgblur=cv2.GaussianBlur(img,(7,7),0)

#canny
#canny methode use for detect egaes
imgcanny=cv2.Canny(imgblur,100,100)

#dilation
""""imgcanny has contours that are not connected 
inoder to get connected contours we use dilate methode"""
kernel=np.ones((3,3),np.uint8)
imgdial=cv2.dilate(imgcanny,kernel,iterations=1)

#erode
imgerod=cv2.erode(imgdial,kernel,iterations=1)

cv2.imshow('img',img)
cv2.imshow('imggray',imggray)
cv2.imshow('imgblur',imgblur)
cv2.imshow('imgcanny',imgcanny)
cv2.imshow('imgdial',imgdial)
cv2.imshow('imgerode',imgerod)
cv2.waitKey(0)