import cv2

img = cv2.imread("klon1.jpg",0)
cv2.imshow("ilkresim",img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

k=cv2.waitKey(0) &0xFF

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("ikinciresim.png",img)
    cv2.destroyAllWindows()