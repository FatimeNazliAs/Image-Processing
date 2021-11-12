import cv2

img = cv2.imread("klon1.jpg")
print(img.shape)


roi = img[30:100,100:400]

cv2.imshow("Klon", img)
cv2.imshow("ROI: ",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
