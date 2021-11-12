
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("img_1.png",0)
"""img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()"""

_,thresh = cv2.threshold(img,100,255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)


cv2.imshow("img",img)
cv2.imshow("THRESH",thresh)
cv2.imshow("THRESH2",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()