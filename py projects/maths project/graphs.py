import cv2
import numpy as np
import math

img=cv2.imread('black.png')


def trigonometry_graphs(scalar='e',plus_or_minus_value='m',function='l'):
    if int(plus_or_minus_value) >= 0:
        mark='+'
    else:
        mark=''
    cv2.line(img,(0,400),(1200,400),(0,255,0),2)
    cv2.line(img,(0,200),(1200,200),(255,0,255),2)
    cv2.line(img,(0,600),(1200,600),(255,0,255),2)
    cv2.putText(img,function+" "+scalar+'X'+" "+mark+plus_or_minus_value, (100,100), cv2.FONT_HERSHEY_PLAIN, 5, (20, 255, 100), 3)

    k=0
    j=0
    coord=[i for i in range(0,360,15)]
    max_v=0
    for i in range(0,360):
        if function=='sin':
            v = math.sin(math.radians(i*int(scalar) + int(plus_or_minus_value)))
        else:
            v = math.cos(math.radians(i*int(scalar) + int(plus_or_minus_value)))



        for h in coord:
            cv2.circle(img, (int(h*(10/3)), 400), 2, (0, 0, 255), 2)
            cv2.putText(img, '{}'.format(h), (int(h * (10 / 3)) - 10, 420), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

        x=int(i * (10 / 3))
        y=(-int(v*200))+400

        if v == 1 or v==-1:
            cv2.line(img,(x,y),(x,400),(255,0,0),2)
            cv2.putText(img, '{}'.format(i), (int(x),int((y+400)/2)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

        elif abs(v)<0.0000001:
            cv2.line(img,(x,200),(x,600),(0,255,0),2)
            cv2.putText(img, '{}'.format(i), (int(x),300), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)


        cv2.circle(img, (x,y), 1, (255, 0, 0), 1)
        cv2.line(img,(k,j),(x,y),(255,255,255),2)
        k,j=x,y

    cv2.imshow('img',img)
    cv2.waitKey(0)




trigonometry_graphs(scalar='3',plus_or_minus_value='-30',function='sin')
