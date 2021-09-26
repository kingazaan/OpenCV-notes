# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 00:23:04 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# images
img = cv.imread(r"Resources/Photos/cats.jpg")
cv.imshow('Cats', img)

# convert this image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur the image 
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

## there are less contours when blurred
# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

##### TODO
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')


## even less contours wehn using a grayscale strategy
# other way  to find contour
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# can also use thresh instead of canny above^^
print(f'{len(contours)} contour(s) found!')


# can draw the contours as well onto a blank canvas
blank = np.zeros(img.shape, dtype='uint8')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)



########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
