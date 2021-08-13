import cv2

img1 = cv2.imread("Z:\\projecttemp\\Python_openCv\\data\\4.jpg",0)
img1 = cv2.resize(img1,(1280,700)) #width
print(img1)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()