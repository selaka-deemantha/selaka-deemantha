import cv2
import numpy as np



def nothing(x):
    pass

cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar',640,240)

cv2.createTrackbar('Hue Min','trackbar',0,179,nothing)
cv2.createTrackbar('Hue Max','trackbar',179,179,nothing)
cv2.createTrackbar('Sat Min','trackbar',57,255,nothing)
cv2.createTrackbar('Sat Max','trackbar',255,255,nothing)
cv2.createTrackbar('Val Min','trackbar',75,255,nothing)
cv2.createTrackbar('Val Max','trackbar',255,255,nothing)

def getcontours(img):
    contours,hierachy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)

        if area>200:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri=cv2.arcLength(cnt,True)
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            number_of_coners=len(approx)#number of coners

            x,y,w,h=cv2.boundingRect(approx)

            if number_of_coners==3:objecttype='Tri'
            elif number_of_coners==4:
                aspratio=w/float(h)
                if aspratio>0.95 and aspratio<1.05:objecttype='square'
                else:objecttype='Triangle'
            elif number_of_coners>4:
                objecttype='circle'

            else:objecttype='None'


            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)




cap=cv2.VideoCapture('banana.mp4')

while True:
    _,img=cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    imgContour = img.copy()


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


    getcontours(mask)

    cv2.imshow('video',imgContour)


    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()