import cv2
import numpy as np
import numpy
#np.uint8 cizim yapilirken kullanılan veri tipi
canvas = np.zeros((512,512,3), dtype=np.uint8)+255







cv2.imshow("Canvas" , canvas)
cv2.waitKey()
cv2.destroyAllWindows()
