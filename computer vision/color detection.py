import cv2
import numpy as np
img=cv2.imread('bv.jpg')
img=cv2.resize(img,(600,500))
def nothing(x):
    pass

cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar',640,240)

cv2.createTrackbar('Hue Min','trackbar',0,179,nothing)
cv2.createTrackbar('Hue Max','trackbar',179,179,nothing)
cv2.createTrackbar('Sat Min','trackbar',58,255,nothing)
cv2.createTrackbar('Sat Max','trackbar',255,255,nothing)
cv2.createTrackbar('Val Min','trackbar',77,255,nothing)
cv2.createTrackbar('Val Max','trackbar',255,255,nothing)

while True:
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos('Hue Min','trackbar')
    h_max = cv2.getTrackbarPos('Hue Max', 'trackbar')
    s_min = cv2.getTrackbarPos('Sat Min', 'trackbar')
    s_max = cv2.getTrackbarPos('Sat Max', 'trackbar')
    v_min = cv2.getTrackbarPos('Val Min', 'trackbar')
    v_max = cv2.getTrackbarPos('Val Max', 'trackbar')

    #print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])

    mask=cv2.inRange(imgHSV,lower,upper)
    imgresult=cv2.bitwise_and(img,img,mask=mask)

    #cv2.imshow('original',img)
    #cv2.imshow('hsv',imgHSV)
    cv2.imshow('mask',mask)
    cv2.imshow('result', imgresult)
    cv2.waitKey(1)