import cv2
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

buffer_size =16
pts = deque(maxlen = buffer_size)

#mavi renk araligi
blueLower = (84, 98, 0)
blueUpper =(179, 255, 255)

#capture
cap = cv2.VideoCapture(0)
cap.set(3,960)
cap.set(4,480)

while True:
    success, imgOriginal = cap.read()

    if success:
        blurred = cv2.GaussianBlur(imgOriginal,(11,11),0)
        #hsv
        hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv image",hsv)

        #mavi icin maske olusturma
        mask = cv2.inRange(hsv,blueLower,blueUpper)
        #cv2.imshow("mask image",mask)
        #maskenin etradında kalan gurultuleri sil
        mask = cv2.erode(mask, None,iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("mask_erozyon_genisleme",mask)

        #kontur
        contours,_ = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        center = None

        if len(contours)>0:
            #en buyuk konturu al
            c = max(contours, key=cv2.contourArea)
            #dikdortgene cevir
            rect = cv2.minAreaRect(c)
            ((x,y),(width,height),rotation) = rect

            s = "x: {}, y: {}, width:{}, height: {}, rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)

            box = cv2.boxPoints(rect)
            box = np.int64(box)

            #moment
            M = cv2.moments(c)
            center =(int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

            #kontur cizdir sari
            cv2.drawContours(imgOriginal,[box],0,(0,255,255),-1)

            #merkeze bir nokta cizdir
            cv2.circle(imgOriginal,center,5,(255,0,255),-1)


            #bilgileri ekrana yazdir
            cv2.putText(imgOriginal,s,(25,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)


        cv2.imshow("orijinal tespit",imgOriginal)






    if cv2.waitKey(1) & 0xFF == ord("q"): break

















