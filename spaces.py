# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:51:16 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# images
img = cv.imread(r"Resources/Photos/cats.jpg")
cv.imshow('Cats', img)

# RGB to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Turn the BGR to HSV
## basically turning an image from being controlled by colors to controlled by characteristics
## in this scenario it is Hue, Saturation, and Value (Brightness)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# turn from BGR to LAB
## LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


# use matplotlib (PLT) to show the image (as a plot basically)
plt.imshow(img)
plt.show()
## image looks weird because BGR is not used in PLT, thats why we convert


# convert BGR to RGB for PLT use
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()


## now lets work backwords
# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
