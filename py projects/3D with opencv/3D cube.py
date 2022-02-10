import cv2
import numpy as np
import math
from mat_math import math_matrix
import time
import random

mat=math_matrix()



projection_matrix=[[1,0,0],[0,1,0],[0,0,0]]

coor=[[[-1],[-1],[1]]  ,[[1],[-1],[1]]  ,[[1],[1],[1]]  ,[[-1],[1],[1]]  ,[[-1],[-1],[-1]]  ,[[1],[-1],[-1]]  ,[[1],[1],[-1]]  ,[[-1],[1],[-1]]]

i_1=0
i_2=0
i_3=0
coor_2d=[mat.mat_mul(projection_matrix,i) for i in coor]

while True:
    color=(0,0,255)
    img = cv2.imread('black.png')
    rotation_x=[[1,0,0],[0,math.cos(math.radians(i_1)),-math.sin(math.radians(i_1))],[0,math.sin(math.radians(i_1)),math.cos(math.radians(i_1))]]
    rotation_y=[[math.cos(math.radians(i_2)),0,math.sin(math.radians(i_2))],[0,1,0],[-math.sin(math.radians(i_2)),0,math.cos(math.radians(i_2))]]
    rotation_z=[[math.cos(math.radians(i_3)),-math.sin(math.radians(i_3)),0],[math.sin(math.radians(i_3)),math.cos(math.radians(i_3)),0],[0,0,1]]

    i_1 += 0.5
    i_2 += 0.5
    i_3 += 0.5
    pp=[]
    for points in coor:
        t=0
        rotate_x=mat.mat_mul(rotation_x,points)
        rotate_y=mat.mat_mul(rotation_y,rotate_x)
        rotate_z=mat.mat_mul(rotation_z,rotate_y)
        point_2d=mat.mat_mul(projection_matrix,rotate_z)

        x=int((point_2d[0][0] * 100) + 300)
        y=int((point_2d[1][0] * 100) + 300)
        pp.append([x,y,t])
        t+=1
    for j in pp:
        cv2.circle(img,(j[0],j[1]),3,color,2)
    for k in range(3):
        cv2.line(img,(pp[k][0],pp[k][1]),(pp[k+1][0],pp[k+1][1]),color,2)
        cv2.line(img,(pp[k+4][0],pp[k+4][1]),(pp[k+5][0],pp[k+5][1]),color,2)
        cv2.line(img,(pp[k][0],pp[k][1]),(pp[k+4][0],pp[k+4][1]),color,2)
    cv2.line(img,(pp[0][0],pp[0][1]),(pp[3][0],pp[3][1]),color,2)
    cv2.line(img, (pp[4][0], pp[4][1]), (pp[7][0], pp[7][1]), color, 2)
    cv2.line(img, (pp[3][0], pp[3][1]), (pp[7][0], pp[7][1]), color, 2)



    cv2.imshow('video',img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

