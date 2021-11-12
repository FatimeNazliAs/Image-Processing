import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("img.png",0)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("img",img)
cv2.imshow("img-th1",th1)
cv2.imshow("img-th2",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()