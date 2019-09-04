#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:07:37 2019

@author: ratnesh
"""
import cv2
import numpy as np

vid = cv2.VideoCapture('./videos/Megamind.avi')
a = 1
while True:
    a = a+1
    check, frame = vid.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', gray)
    cv2.waitKey(1)
    
#    if key == ord('q'):
        
    
#print(check)
#cv2.imshow('Video', frame)
print(a)
vid.release()

cv2.destroyAllWindows()
