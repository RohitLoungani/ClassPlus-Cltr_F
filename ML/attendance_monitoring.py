# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:47:03 2021

@author: Yash
"""
import numpy as np
import pandas as pd
import cv2
import face_recognition
import pickle
from pickle import load, dump
import os
import datetime
import math
import textwrap
from live_detection import liveness_detection
from attendance_register import take_attendance
from PIL import Image, ImageDraw

with open("image_encodings.pkl", "rb") as f:
    image_encodings = load(f)

with open("names.pkl", "rb") as f:
    names = load(f)
print(image_encodings)

#For attendance

def check_attendance(name):
    #with open("image_encodings.pkl", "rb") as f:
    #    image_encodings = loads(f.read())
    print(image_encodings)
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
                cv2.imshow('Capturing', frame)
                text = "If you want to retake your image, press space bar."
                font = cv2.FONT_HERSHEY_TRIPLEX
                textsize = cv2.getTextSize(text, font, 1, 2)[0]
                x = int((frame.shape[1] - textsize[0])/2) + 200
                y = int((frame.shape[0] - textsize[1])/2) + 225
                cv2.putText(frame, text, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.imshow('Capturing', frame)
                while(cv2.waitKey(1) == -1):
                    cv2.imshow('Capturing', frame)
                if(cv2.waitKey(1) == 32):
                    continue
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_loc = face_recognition.face_locations(frame)
                encodings = face_recognition.face_encodings(frame, face_loc)
                result = face_recognition.compare_faces(image_encodings, np.array(encodings))
                dist = face_recognition.face_distance(image_encodings, np.array(encodings))
                if(result == False):
                    print("No match found. Try again!!!")
                    continue
                else:
                    text = "Match found. Proceed for liveness detection test."
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    textsize = cv2.getTextSize(text, font, 1, 2)[0]
                    x = int((frame.shape[1] - textsize[0])/2) + 300
                    y = int((frame.shape[0] - textsize[1])/2) + 200
                    #text = textwrap.wrap(text, 60)
                    cv2.putText(frame, text, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                
                    print("Match found.")
                    best_match = np.argmin(dist)
                    match = face_recognition.compare_faces(image_encodings, encodings[0])
                    dist = face_recognition.face_distance(image_encodings, encodings[0])
                    best_match = np.argmin(dist)
                    person = ""
                    if(result[best_match]):
                            person = names[best_match]
                    pil_image = Image.fromarray(frame)
                    # Create a Pillow ImageDraw Draw instance to draw
                    draw = ImageDraw.Draw(pil_image)
                    for (top, right, bottom, left),_ in zip(face_loc, encodings):
                        match = face_recognition.compare_faces(image_encodings, encodings[0])
                        dist = face_recognition.face_distance(image_encodings, encodings[0])
                        best_match = np.argmin(dist)
                        person = ""
                        if(result[best_match]):
                            person = names[best_match]
                        
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255))
                        w, h = draw.textsize(person)
                        font = cv2.FONT_HERSHEY_TRIPLEX
                        cv2.rectangle(frame, (left, bottom - h - 10), (right, bottom), (0, 0, 255), 1)
                        cv2.putText(frame, person, (left + 6, bottom - h - 5), font, 1, (0, 0, 255), 2)
                        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                        while(cv2.waitKey(1) == -1):
                            cv2.imshow('Capturing', frame)
                        #display(pil_image)
                    print(result, dist)
                    
                    
                    flag = 0
                    if(liveness_detection(flag) == 0):
                        print(flag)
                        text = "Don't try to cheat, kid!!! Login again."
                        font = cv2.FONT_HERSHEY_TRIPLEX
                        textsize = cv2.getTextSize(text, font, 1, 2)[0]
                        x = int((frame.shape[1] - textsize[0])/2) + 500
                        y = int((frame.shape[0] - textsize[1])/2) + 200
                        #text = textwrap.wrap(text, 60)
                        cv2.putText(frame, text, (x, y), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
                        print("Don't try to cheat, kid!!! Login again.")
                        break                        
                        
                    print("Hi {0}, your attendance has been recorded.".format(person))
                    take_attendance(person)

                    capture.release()
                    cv2.destroyAllWindows()
                    break

        else:
            #print("Unable to open camera. Try again!!!")
            break
    return flag