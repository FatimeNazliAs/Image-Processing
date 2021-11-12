import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.figure(),plt.imshow(img_vis)



img_hist = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
color =("b","g","r")
#plt.figure()
for i, c in enumerate(color):
    hist = cv2.calcHist([img],channels=[i],mask=None,histSize=[256],ranges=[0,256])
    plt.plot(hist, color =c)

golden =cv2.imread("goldenGate.jpg")
golden_vis=cv2.cvtColor(golden,cv2.COLOR_BGR2RGB)
#plt.figure(),plt.imshow(golden_vis)
print(golden.shape)

mask = np.zeros(golden.shape[:2], np.uint8)
#plt.figure(),plt.imshow(mask, cmap ="gray")

mask[1500:2000,1000:2000] = 255
#plt.figure(),plt.imshow(mask, cmap ="gray")

masked_img_vis = cv2.bitwise_and(golden_vis,golden_vis,mask=mask)
#plt.figure(),plt.imshow(masked_img_vis, cmap ="gray")


masked_img =cv2.bitwise_and(golden,golden,mask=mask)
masked_img_hist= cv2.calcHist([golden],channels=[0],mask=None,histSize=[256],ranges=[0,256])
#plt.figure(),plt.plot(masked_img_hist)

#histogram esitleme

img1 = cv2.imread("hist_equ.jpg",0)
plt.figure(),plt.imshow(img1, cmap ="gray")

img_hist = cv2.calcHist([img1],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(),plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img1)
plt.figure(),plt.imshow(eq_hist , cmap ="gray")

plt.show()