# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:59:55 2021

@author: ab
"""

import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# have a blank canvas
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# paint canvas a specific color with the fRGB values
blank[:] = 0, 0, 255
cv.imshow("Window - Red ", blank)

# can also color within canvas
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("Red box inside Black ", blank)


# different shapes - lets do a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangle', blank)

# draw a circle 
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
# cv.imshow('Circle', blank)

# draw a line
cv.line(blank, (100,250), (300, 400), (250, 250, 255), thickness=3)
# cv.imshow('Line', blank)

# write text on the image
cv.putText(blank, 'I am ur mother pal!!!', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
