import cv2
import numpy as np

img=cv2.imread('shapes.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

coners=cv2.goodFeaturesToTrack(gray,27,0.01,10)

for i in coners:
    x,y=i.ravel()
    cv2.circle(img,(int(x),int(y)),2,(255,0,0),cv2.FILLED)

cv2.imshow('image',img)
cv2.waitKey(0)