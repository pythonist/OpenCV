import cv2
import numpy as np

img = cv2.imread("porsche.jpg")
#print(img.shape)

#defining a kernel for dilation
kernel = np.ones((5,5),np.uint8)
#gray image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur image
imgBlur = cv2.GaussianBlur(imgGray,(9,9),0)

#canny edge detector
imgCanny = cv2.Canny(img,140,150)

#dilate increases the obejct area in the image
imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)

#erode the image
imgErode = cv2.erode(imgDilate,kernel,iterations=1)

#resizizng the image
imgResize = cv2.resize(img,(600,500))

#cropping the image
imgCropped = img[0:300,0:300]

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilated Image",imgDilate)
cv2.imshow("Eroded Image",imgErode)
cv2.imshow("Car",img)
cv2.imshow("Resized Car",imgResize)
cv2.imshow("Cropped Image",imgCropped)
#print(imgResize.shape)
cv2.waitKey(0)

