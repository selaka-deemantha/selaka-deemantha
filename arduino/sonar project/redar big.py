import cv2
import numpy as np
import math
import time
import random

img=cv2.imread('black.png')

#x**2 + y**2 = 1
color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
i=0
x=600
y=1

while True:
    l=random.randint(0,400)
    sin=math.sin(math.radians(i))
    cos=math.cos(math.radians(i))
    x_=x+400*sin
    y_ = y + 400 * (1-cos)

    m=l/400
    n=1-m

    X=(1/(m+n))*(n*600 + m*x_)
    Y = (1 / (m + n)) * (n * 400 + m * y_)

    cv2.line(img, (int(X), int(Y)), (600, 400), color, 2)
    cv2.circle(img,(600,400),400,(255,0,0),3)

    cv2.imshow('video',img)
    if i==360:
        i=0
        img=cv2.imread('black.png')
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    i+=5

    time.sleep(0.1)



    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()