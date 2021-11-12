import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

while  True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensitivity =15
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])


    mask = cv2.inRange(hsv, lower_white, upper_white)
    res=cv2.bitwise_and(frame,frame,mask=mask)


    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



