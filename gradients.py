# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:51:58 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# images
img = cv.imread(r"Resources/Photos/park.jpg")
cv.imshow('Park', img)

# turn image gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian - basically penciled edges of an image
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)


cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel', combined_sobel)

# compare Lablacian and SObel with Canny

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows(

