"""
Advanced Cv2
"""
import cv2
import numpy as np

img = cv2.imread("card.jpg")

width, height= 250,350
#warping the image out of an image
#defining the corners or cordinates of the image we want
pt1 = np.float32([[811,191],[1044,332],[596,561],[832,693]])
#defininf cordinates to display them straight
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Card",img)
cv2.imshow("Warp Image",imgOutput)
cv2.waitKey(0)



