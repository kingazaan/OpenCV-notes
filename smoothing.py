# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:14:11 2021

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

# Averaging Blur
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Blur', blur)

# Median Blur (usually better than averageing blur)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blue (takes more data into account basically)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)



########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()

