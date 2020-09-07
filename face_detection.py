#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Import cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Define video capture object
vc = cv2.VideoCapture(0)

#Image capture loop
if vc.isOpened(): # try to get the first frame
    is_capturing, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    # makes the blues image look real colored
    webcam_preview = plt.imshow(frame)    
else:
    is_capturing = False 

def get_face_location():

    is_capturing, frame = vc.read()
    #Convert colours
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    try:
        #Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    except:
        return #no faces
    else: 
        #Add ROI rectangles
        for (x,y,w,h) in faces:
            # frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            # print("X coordinate: " + str(x))
            # print("Y coordinate: " + str(y))

            return x, y