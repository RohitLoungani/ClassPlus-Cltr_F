# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:56:25 2021

@author: Yash
"""

import numpy as np
from pickle import load, dump
from flask import Flask, request
from flasgger import Swagger
import registration
import attendance_monitoring

app = Flask(__name__)
Swagger(app)

with open("image_encodings.pkl", "rb") as f:
    image_encodings = load(f)
print(image_encodings)

@app.route('/')
def welcome():
    return "Welcome to ClassPlus!!!"

@app.route('/registration')
def registration_process():
    
    """Pls register yourself, to enter any class.
    ---
    parameters:
        - name: name
          in: query
          type: string
          required: true
        - name: phone
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
        
    """
    name = request.args.get('name')
    phone = request.args.get('phone')
    registration.register(name)
    return name + ", you have successfully registered."

@app.route('/attendance')
def attendance_process():
    """Your attendance needs to be marked before you enter the classroom.
    ---
    parameters:
        - name: name
          in: query
          type: string
          required: true
        - name: phone
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
    """
    name = request.args.get('name')
    phone = request.args.get('phone')
    flag = attendance_monitoring.check_attendance(name)
    if flag:
        return "Hi" + name + ", your attendance has been recorded."
    return "Don't try to cheat, kid!!! Login again."
    

if __name__ == '__main__':
    app.run()



