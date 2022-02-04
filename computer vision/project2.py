import cv2
import numpy as np

object_detector=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)
cap=cv2.VideoCapture('v.mp4')

while True:
    _,img=cap.read()

    detections = []

    mask = object_detector.apply(img)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # calculate area and remove small element
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(roi,[cnt],-1,(0,255,0),2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('video',img)


    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()