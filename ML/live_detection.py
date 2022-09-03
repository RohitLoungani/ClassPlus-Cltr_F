# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:28:51 2021

@author: Yash
"""

import numpy as np
import pandas as pd
import cv2
import face_recognition
import pickle
from pickle import loads, dumps
import os
import datetime
import math
import textwrap

def liveness_detection(flag):
    
    def lip_height(lip):
        sum = 0
        for i in [2, 3, 4]:
            dist = math.sqrt((lip[i][0] - lip[12-i][0])**2 + (lip[i][1] - lip[12-i][1])**2)
            sum += dist
        return sum/3
    
    def mouth_height(top_lip, bottom_lip):
        sum = 0
        for i in [8, 9, 10]:
            dist = math.sqrt((top_lip[i][0] - bottom_lip[18-i][0])**2 + (top_lip[i][1] - bottom_lip[18-i][1])**2)
            sum += dist
        return sum/3
    
    def detect_open_mouth(face_landmarks):
        top_lip = face_landmarks['top_lip']
        bottom_lip = face_landmarks['bottom_lip']
        
        top_lip_h = lip_height(top_lip)
        bottom_lip_h = lip_height(bottom_lip)
        mouth_h = mouth_height(top_lip, bottom_lip)
        
        if(mouth_h > min(top_lip_h, bottom_lip_h)*0.5):
            return True
        else:
            return False  
        
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        counter = 1
        target = 11
        while ret == True:
            if(counter == target):
                ret, frame = capture.read()
                #print("Open your mouth for liveness detection test.")
                text = "Open your mouth for liveness detection test."
                font = cv2.FONT_HERSHEY_TRIPLEX
                textsize = cv2.getTextSize(text, font, 1, 2)[0]
                x = int((frame.shape[1] - textsize[0])/2) + 250
                y = int((frame.shape[0] - textsize[1])/2) + 200
                #text = textwrap.wrap(text, 60)
                cv2.putText(frame, text, (x, y), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.imshow('Capturing', frame)
                counter = 0
            else:
                ret = capture.grab()
                counter += 1
            if(cv2.waitKey(1) == 13):                
                text = "If you want to retake your image, press space bar."
                font = cv2.FONT_HERSHEY_TRIPLEX
                textsize = cv2.getTextSize(text, font, 1, 2)[0]
                x = int((frame.shape[1] - textsize[0])/2) + 250
                y = int((frame.shape[0] - textsize[1])/2) + 230
                #text = textwrap.wrap(text, 60)
                cv2.putText(frame, text, (x, y), font, 0.3, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.imshow('Capturing', frame)
                while(cv2.waitKey(1) == -1):
                    cv2.imshow('Capturing', frame)
                if(cv2.waitKey(1) == 32):
                    continue
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_landmarks = face_recognition.face_landmarks(frame)
                
                print(face_landmarks[0])
                if(detect_open_mouth(face_landmarks[0])):
                    print("Liveness detection test passed.")
                    flag = 1
                
                
                capture.release()
                cv2.destroyAllWindows()
                break

        else:
            #print("Unable to open camera. Try again!!!")
            break
    return flag