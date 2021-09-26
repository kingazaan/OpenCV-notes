# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:04:32 2021

@author: ab
"""
import cv2 as cv
import os

# set current working director

os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

## Resizing photos

# read in photo

# window_name = 'Cat'
# img = cv.imread(r"Resources/Photos/cat_large.jpg")
# cv.imshow(window_name, img)

# rescale function

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

## Resizing videos

# read in video

capture = cv.VideoCapture(r"Resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow("Video", frame)
    cv.setWindowProperty("Video", cv.WND_PROP_TOPMOST, 1)
    cv.imshow("Video Resized", frame_resized)
    cv.setWindowProperty("Video Resized", cv.WND_PROP_TOPMOST, 1)
    
    # cv.setWindowProperty(window_name, cv.WND_PROP_TOPMOST, 1)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# alternate way to resize videos
# BUT only works for live videos

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


##

# ending functions

capture.release()
cv.waitKey(0)
cv.destroyAllWindows()