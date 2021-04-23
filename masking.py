import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",600,300)
cv2.createTrackbar("Hue Min","TrackBar",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBar",179,179,empty)
cv2.createTrackbar("Saturation Min","TrackBar",63,255,empty)
cv2.createTrackbar("Saturation Max","TrackBar",255,255,empty)
cv2.createTrackbar("Value Min","TrackBar",48,255,empty)
cv2.createTrackbar("Value Max","TrackBar",255,255,empty)

while True:
    img = cv2.imread('lambo.png')
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBar")
    s_min = cv2.getTrackbarPos("Saturation Min","TrackBar")
    s_max = cv2.getTrackbarPos("Saturation Max","TrackBar")
    v_min = cv2.getTrackbarPos("Value Min","TrackBar")
    v_max = cv2.getTrackbarPos("Value Max","TrackBar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    
    
    cv2.imshow("Car",img) 
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("And Image",imgResult)
    cv2.imwrite("Maskedimage.jpg",imgResult)
    cv2.imwrite("HSV.jpg",imgHSV)
    cv2.imwrite("Mask.jpg",mask)
    cv2.waitKey(1)



