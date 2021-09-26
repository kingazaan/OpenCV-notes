# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:36:20 2021

@author: ab
"""
import cv2 as cv
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# use the haar_cascade xml file to make an actual classifier variable
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# capture video (use 0 for webcam)
cap = cv.VideoCapture(r"Resources/Videos/sample.mp4")

# use loop to convert video images to grayscale 
while True:
    _, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # use the haar cascade from the OpenCV file
    faces = haar_cascade.detectMultiScale(gray, 1.4, 9)
    ## bigger scale factor = faster but less accurate
    ## more neighbors means higher quality but less detection
    
    # loop
    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    
    cv.imshow('img', img)
    
    # break loop if escape key is pressed
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

# release the camera
cap.release()



########################
# ending functions

cv.destroyAllWindows()

