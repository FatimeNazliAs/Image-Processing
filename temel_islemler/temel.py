import cv2
import numpy as np


img = cv2.imread("klon1.jpg")
dimension = img.shape #boyutları gosterir
print(dimension)
color = img[420, 500]
print(color)

blue = img[420,500,0]
print("blue:", blue)

green = img[420,500,1]
print("green: ", green)

red = img[420,500,2]
print("red: ", red)


new_blue= img. item(150,200,0)
print("blue: ",new_blue)
img.itemset((150,200,0),172)
print("new blue: ",img[150,200,0])


#cv2.imshow("klon asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
