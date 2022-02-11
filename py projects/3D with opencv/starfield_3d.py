import random
import cv2
import numpy as np
from mat_math import math_matrix
import time

mat=math_matrix()

img = np.zeros([800, 1500, 3])


class star():
    def __init__(self):
        self.height = 800
        self.width = 1500
        self.x=random.randint(0,1500)
        self.y = random.randint(0,800)
        self.z =random.randint(2,1000)

    def draw(self):
        cv2.circle(img,(self.x,self.y),3,(0,255,0),2)

    def move(self):
        if self.z<=0:
            self.z=self.width
        self.x_=((self.x-800)/self.z)*1500
        self.y_ = (-(self.y-450) / self.z)*800
        self.z -=10

        cv2.circle(img,(int(750-self.x_),int(400-self.y_)),3,(0,255,0),2)
        if self.x_==1490 or self.y_==790 or self.x_==10 or self.y_==10:
            self.x = random.randint(0, 1500)
            self.y = random.randint(0, 800)



obj=[]
for i in range(300):
    i=star()
    i.draw()

    obj.append(i)

l=0
while True:
    img = np.zeros([800, 1500, 3])
    for i in obj:
        i.move()



    cv2.imshow('img',img)
    cv2.waitKey(1)



