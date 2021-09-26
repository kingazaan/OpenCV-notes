# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:39:28 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# images
img = cv.imread(r"Resources/Photos/cat.jpg")
cv.imshow('Cat', img)

# make a mask for the image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

# masking
mask = cv.circle(blank, (img.shape[1]//2 + 65, img.shape[0]//2), 100, 225, -1)
cv.imshow('Mask', mask)

# masking an image to hide part of the image
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Masked', masked)

## start to make a weird shape to see how it looks
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 65, img.shape[0]//2), 100, 255, -1)


weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
