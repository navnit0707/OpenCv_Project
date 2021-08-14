# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 11:50:05 2021

@author: Navneet
"""
import cv2

path = input("enter the path and the name of an image===" )
print("you enter this ===",path)

#reading image
img1 = cv2.imread(path,0) #convert image int graysale
img1 = cv2.resize(img1,(500,500))

cv2.imshow("converted image ==",img1)

k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("Z:\projecttemp\Python_openCv\convert_img_gray\output.png",img1)
else:
    cv2.destroyAllWindows()