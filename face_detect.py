# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:47:03 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# images
img = cv.imread(r"Resources/Photos/waldo.jpg")
cv.imshow('Group', img)

# convert to gray
## needs to be gray for face detection
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

# use the haar_cascade xml file to make an actual classifier variable
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# detect a face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

# lets make a drawn rectangle over every face
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces', img)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()

