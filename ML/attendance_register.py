# -*- coding: utf-8 -*-
"""
Created on Sun May  2 02:21:05 2021

@author: Yash
"""
import datetime
import os

def take_attendance(student):
    if not os.path.isfile("attendance_regsiter.csv"):
        f = open("attendance_regsiter.csv", "a")
        f.close()
    with open("attendance_regsiter.csv", 'r+') as f:
        attendance_list = f.readlines()
        all_names = []
        for name in attendance_list: 
            all_names.append(name.split(',')[0])
        if student not in all_names:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            f.writelines(f'\n {student}, {time}')
            
