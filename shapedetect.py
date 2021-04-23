import cv2
import numpy as np

def getCountours(imgResize):
    contours,hierarchy = cv2.findContours(imgResize,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i)
        print(area)
        if area>500:
             cv2.drawContours(imgContour,i,-1,(255,0,0),3)
             peri = cv2.arcLength(i,True)
             #print(peri)
             approx = cv2.approxPolyDP(i,0.02*peri,True)
             print(len(approx))
             objCor = len(approx)
             x, y, w, h = cv2.boundingRect(approx)
             if objCor ==3: objectType ="Tri"
             elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rect"
             elif objCor>4: objectType= "Circle"
             else:objectType="None"



             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
             cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
             
            

img = cv2.imread("shape detect/shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,60,60)
getCountours(imgCanny)

#cv2.imshow("Shapes",img)
#cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contours",imgContour)
cv2.imwrite("ShapeOutput.jpg",imgContour)
cv2.waitKey(0)
