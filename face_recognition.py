# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:27:43 2021

@author: ab
"""
import numpy as np
import cv2 as cv
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# make list to get all names in Faces/train folder
people = []
for i in os.listdir(r"\Users\ab\Documents\GitHub\OpenCV-notes\Resources\Faces\train"):
    people.append(i)

# load the numpy arrays to be used elsewhere
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r"C:\Users\ab\Documents\GitHub\OpenCV-notes\Resources\Faces\val\ben_afflek\2.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {people[label]} with a confidence interval of {confidence}")
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
