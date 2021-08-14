import cv2

img1 = cv2.imread("Z:\\projecttemp\\Python_openCv\\data\\4.jpg",1) #1 for original
img1 = cv2.resize(img1,(1280,700)) #width
print(img1)
cv2.imshow("original",img1)

#cv2 to read imagein gray

img2 = cv2.imread('Z:\\projecttemp\\Python_openCv\\data\\4.jpg',0) #0 for gray
img2 = cv2.resize(img2,(1280,700)) #width , height
cv2.imshow("gray scale image",img2)
print("image in gray scale ==\n",img2) 

cv2.waitKey()
cv2.destroyAllWindows()