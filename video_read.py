# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:28:48 2021

@author: Navneet
"""

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("Z:\\projecttemp\\Python_openCv\\data\\output.avi",fourcc,20.0,(640,480),0)

print(cap)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        if cv2.waitKey(1)&0xFF == ord("q"):
            break
cap.release()
output.realease()
cv2.destroyAllWindows( )
