"""
Test code for Spike Timer.
Implements openCV to detect spike on screen.
Refer this link: https://tinyurl.com/wszwzszs
"""

import cv2 as cv
import numpy as np
import pyautogui
from PIL import Image

img = Image.open(r"Imgs\VALORANT-Win64-Shipping_1625154476.jpg") # Img to be checked for spike

#Use the below piece of code to crop only the spike indicator region.
#area = 914,14,914+90,14+93  
#img = img.crop(area)

open_cv_image = np.array(img)  # converting the img to cv image format
open_cv_image = open_cv_image[:, :, ::-1].copy() 

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

spike_img = cv.imread(r'C:\Users\Gokul Ram\Desktop\Spike Timer\spike1.jpg') # The sample spike image

match_result = cv.matchTemplate(open_cv_image,spike_img,cv.TM_CCOEFF_NORMED)
cv.namedWindow('Result',cv.WINDOW_NORMAL) 
cv.imshow('Result',match_result) #Brings up a window that shows various spots of matches. 
#The brightest part(spot) represents the closest match.
cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(match_result)
print(max_loc) #Location of the brightest spot
print(max_val) #Confidence level of the match





