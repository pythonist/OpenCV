import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)
#print(img)

#B #G #R channel is used in cv2 
#coloring specific region
#img[400:500,0:600] = 0,204,0

#drawing lines(img,starting point,width,height,color,thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),2)
cv2.line(img,(10,60),(img.shape[1],img.shape[0]),(0,255,255),3)

#drawing rectangle(img,starting point,size,color,thickness/filled)
cv2.rectangle(img,(0,0),(200,300),(255,178,107),4)
cv2.putText(img,"OpenCV Tutorial",(300,100),cv2.FONT_ITALIC,1,(255,255,255),2)
cv2.circle(img,(300,30),20,(0,204,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)