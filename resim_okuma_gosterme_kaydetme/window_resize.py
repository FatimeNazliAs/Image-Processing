import cv2

#cv2.namedWindow("klon")
img = cv2.imread("klon1.jpg")
img = cv2.resize(img,(640,480))
cv2.imshow("klon",img)
img1 = img[0:200,0:300]#yukseklik,genislik
cv2.imshow("kirpilmis resim",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
