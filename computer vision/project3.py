import cv2

import numpy as np
cap=cv2.VideoCapture(0)


def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3,1)
    cv2.putText(img, "Trackin", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


tracker=cv2.TrackerCSRT_create()
success,img=cap.read()
bbox=cv2.selectROI('Tracking',img,False)
tracker.init(img,bbox)


while True:
    timer=cv2.getTickCount()
    success,img=cap.read()
    success,bbox=tracker.update(img)

    if success:
        drawbox(img,bbox)
    else:

        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    cv2.imshow('video', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()



