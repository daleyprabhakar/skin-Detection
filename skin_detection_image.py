# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:17:10 2018

@author: s.prabhakar.daley
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
input_imgs = ['LightDark5.png', 'white5.jpg']
output_imgs = ['LightDark5_det', 'white5_det']
for i in range(0,len(input_imgs)):
    # Convert BGR image to HSV image format
    raw_image= cv2.imread(input_imgs[i])
    hsv = cv2.cvtColor(raw_image, cv2.COLOR_BGR2HSV)
    #hsv hue sat value metrics for filtering of the image
    lower = np.array([0, 48, 80])
    upper = np.array([20, 255, 255])
    #Masking of image based on lower and upper limits
    mask = cv2.inRange(hsv, lower, upper)
    # Taking the image of only filtered pixels
    res = cv2.bitwise_and(raw_image, raw_image, mask= mask)
    #visualizating the image
    outputpath = output_imgs[i]+'.jpg'
    cv2.imwrite(outputpath, res)



