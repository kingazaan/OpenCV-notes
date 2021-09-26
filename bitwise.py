# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:30:08 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")


blank = np.zeros((400,400), dtype='uint8')

# lets draw out a circle and rectangle on blank canvas
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Using bitwise AND to combine images (like inner join)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And', bitwise_and)

# Using bitwise OR to combine images (like outer join)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise Or', bitwise_or)

# Using bitwise XOR to combine images (like outer join minus inner join)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise Xor', bitwise_xor)

# Using bitwise Not to inverse image basically
bitwise_not = cv.bitwise_not (rectangle)
cv.imshow('Bitwise Not', bitwise_not )




########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
