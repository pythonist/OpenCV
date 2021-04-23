import cv2

wCam,hCam = 1280,720


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()
    
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyWindow('Video')
