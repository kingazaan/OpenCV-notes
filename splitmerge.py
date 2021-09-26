# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 01:26:13 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# images
img = cv.imread(r"Resources/Photos/park.jpg")
cv.imshow('Boston', img)

# split image into base colors
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape, b.shape, g.shape, r.shape)

# lets try and merge theese pictures together
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

# create blank canvas 
blank = np.zeros(img.shape[:2], dtype='uint8')

# merge again using a blank canvas, so that we can see the actual colors of the images

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r]) 

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()



