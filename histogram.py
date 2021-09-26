# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:58:54 2021

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
cv.imshow('Cat', img)

# convert image to grayscale first
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# make a blank mask
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2 + 15, img.shape[0]//2), 100, 225, -1)
# mask = cv.bitwise_and(gray, gray, mask=circle)

# cv.imshow('Mask', mask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
# can see for different images, grayscale histograms show which colors are dominant

##########
# Now lets do color

# make mask for color now

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

# show histogram for area that is mask
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
