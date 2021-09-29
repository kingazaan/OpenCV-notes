# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:51:46 2021

@author: ab
"""
import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")

# make list to get all names in Faces/train folder
p = []
for i in os.listdir(r"\Users\ab\Documents\GitHub\OpenCV-notes\Resources\Faces\train"):
    p.append(i)

# save base train folder
DIR = r"\Users\ab\Documents\GitHub\OpenCV-notes\Resources\Faces\train"

# use the haar_cascade xml file to make an actual classifier variable
haar_cascade = cv.CascadeClassifier('haar_face.xml')


features = []

# create labels to save the index for every picture
labels = []

# now we can create an save paths for every person in the train folder
def create_train():
    for i in p:
        # making path to each person's folder
        path = os.path.join(DIR, i)
        label = p.index(i)
        
        # making path for EVERY IMAGE
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            # make all images gray
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            # detect a face
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            # Create boxes around every face we find
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                
                # append to 
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------------------')

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

# Convert both featrues and labels to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

# Train Recognizer on features and labels list
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

# save the trained model as a yml
face_recognizer.save('face_trained.yml')

# save the numpy arrays to be used elsewhere
np.save('features.npy', features)
np.save('labels.npy', labels)


########################
# ending functions

cv.waitKey(0)
cv.destroyAllWindows()
