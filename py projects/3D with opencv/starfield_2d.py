import random
import cv2
import numpy as np

img = np.zeros([800, 1500, 3])


class star():
    def __init__(self):
        self.co=[]
        self.height = 800
        self.width = 1500
        self.x=random.randint(1500,3500)
        self.y = random.randint(800, 2800)
        self.z = random.randint(0, self.width)
        self.k=0

    def draw(self):
        cv2.circle(img,(self.x,self.y),3,(0,255,0),2)

    def move(self,k=3):
        self.x -=k
        self.y -=k-1
        cv2.circle(img,(self.x,self.y),3,(0,255,0),2)
        if self.x==0 or self.y==0:
            self.x=random.randint(1500,2500)
            self.y = random.randint(800, 1800)
obj=[]
for i in range(400):
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
