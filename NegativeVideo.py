import cv2
import numpy as np

##Img=cv2.imread('1.jpg');
cap = cv2.VideoCapture(0)
while 1:
    ret,img = cap.read()
    imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Img=img;
    cv2.imshow('Original Image',Img);
    Red_Plane=Img[:,:,2];
##cv2.imshow('original Image',Img);
    r,c=Red_Plane.shape;
    op=np.zeros((r,c),dtype=np.uint8);
    for i in range(0,r-2):
        for j in range(0,c-2):
            partimg=-1*Red_Plane[i,j]
            op[i,j]=partimg;
    cv2.imshow('Image Negative',op);
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
