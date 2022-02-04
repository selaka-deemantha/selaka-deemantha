import cv2
import numpy as np

def getcontours(img):
    contours,hierachy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)

        if area>500:
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
            cv2.putText(imgContour,objecttype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)



img =cv2.imread('shapes.jpg')
imgContour=img.copy()


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(7,7),1)
canny=cv2.Canny(blur,50,50)
getcontours(canny)
blank=np.zeros_like(img)


cv2.imshow('image',img)
cv2.imshow('imagegray',gray)
cv2.imshow('imagegray',imgContour)
cv2.waitKey(0)