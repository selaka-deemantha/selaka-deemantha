import cv2
import math
import time
import random




#x**2 + y**2 = 1
color=(255,0,0)
i=0
img=cv2.imread('OIP.jpg')
x=120
y=20

while True:
    l=random.randint(0,100)
    sin=math.sin(math.radians(i))
    cos=math.cos(math.radians(i))
    x_=x+100*sin
    y_ = y + 100 * (1-cos)

    m=l/100
    n=1-m

    X=(1/(m+n))*(n*120 + m*x_)
    Y = (1 / (m + n)) * (n * 120 + m * y_)

    cv2.line(img, (int(X), int(Y)), (120, 120), color, 1)
    cv2.circle(img,(120,120),100,(255,0,0),3)

    cv2.imshow('video',img)
    if i==360:
        i=0
        color=(0,255,0)
    i+=5
    time.sleep(0.2)



    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()