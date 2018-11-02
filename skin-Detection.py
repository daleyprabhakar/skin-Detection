# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:17:10 2018

@author: s.prabhakar.daley
"""

import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    ret , frame=cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #hsv hue sat value
    lower = np.array([0, 48, 80])
    upper = np.array([20, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    #visualization
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
