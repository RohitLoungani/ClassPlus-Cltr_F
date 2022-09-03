# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:24:45 2021

@author: Yash
"""

import numpy as np
import cv2
import face_recognition
import pickle
from pickle import load, dump

image_encodings = []
names = []
# For registration

def register(name):
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        counter = 1
        target = 11
        while ret == True:
            if(counter == target):
                ret, frame = capture.read()
                cv2.imshow('Capturing', frame)
                counter = 0
            else:
                ret = capture.grab()
                counter += 1
            if(cv2.waitKey(1) == 13):
                text = "If you want to retake your image, press space bar."
                font = cv2.FONT_HERSHEY_TRIPLEX
                textsize = cv2.getTextSize(text, font, 1, 2)[0]
                x = int((frame.shape[1] - textsize[0])/2) + 150
                y = int((frame.shape[0] - textsize[1])/2) + 250
                cv2.putText(frame, text, (x, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.imshow('Capturing', frame)
                while(cv2.waitKey(1) == -1):
                    cv2.imshow('Capturing', frame)
                if(cv2.waitKey(1) == 32):
                    continue
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_loc = face_recognition.face_locations(frame)
                encodings = face_recognition.face_encodings(frame, face_loc)[0]
                print(encodings)
                image_encodings.append(encodings)
                names.append(name)
                print(image_encodings)
                print("{0}, you have successfully registered.".format(name))

                capture.release()
                cv2.destroyAllWindows()
                break

        else:
            #print("Unable to open camera. Try again!!!")
            break
            
    #with open("image_encodings.pkl", "wb") as f:
    dump(image_encodings, open("image_encodings.pkl", "wb"))
    dump(names, open("names.pkl", "wb") )
    #f = open("image_encodings.dat", "wb")
    #dump(image_encodings, f)
    #f.close()
    
