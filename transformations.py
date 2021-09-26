# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 00:13:51 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# choose image
img = cv.imread(r"Resources\Photos\park.jpg")
cv.imshow('Boston', img)

# Translate this image
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x is left, while x is right. Same with y and y for up/down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotate the image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated Image', rotated)

# Flip an image
flip = cv.flip(img, -1)
cv.imshow('Flipped', flip)

########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
