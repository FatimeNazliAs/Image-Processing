import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8)+255

cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5) #baslangic,bitis,renk,kalinlik
cv2.line(canvas,(200,50),(250,512),(255,300,0),40)

cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),-1)#sol üst kose,csag alt kose, renk, kalinlik

cv2.circle(canvas,(250,250),100,(0,0,255),-1 )#merkez,yaricap,renk,kalinlik


p1=(100,200)
p2=(50,50)
p3=(300,100)

cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)

points = np.array([[110, 200],[330,200],[290,220],[100,100]],np.int32)
cv2.polylines(canvas,[points],True,(0,0,100),5)#cokgen





cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
