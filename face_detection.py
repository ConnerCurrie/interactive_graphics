#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":

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

    while is_capturing:
        try:    # Lookout for a keyboardInterrupt to stop the script
            is_capturing, frame = vc.read()
            #Convert colours
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            try:
                #Detect faces
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            except:
                pass #no faces
            else: 
                #Add ROI rectangles
                for (x,y,w,h) in faces:
                    # frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    print("X coordinate: " + str(x))
                    print("Y coordinate: " + str(y))
                    # roi_gray = gray[y:y+h, x:x+w]
                    # roi_color = frame[y:y+h, x:x+w]
                    # eyes = eye_cascade.detectMultiScale(roi_gray)
                    
                    # for (ex,ey,ew,eh) in eyes:
                    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
            #Output to plot
            # plt.imshow(frame)
            # plt.show()
            
        except KeyboardInterrupt:
            vc.release()