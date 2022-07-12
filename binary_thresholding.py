import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("org2.png",0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img = clahe.apply(img)

plt.hist(cl_img.flat, bins = 100, range=(100,255))
#plt.show()

ret, thresh1 = cv2.threshold(cl_img, 150,250, cv2.THRESH_BINARY)

ret2, thresh2 = cv2.threshold(cl_img, 50,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

ret3, thresh3 = cv2.threshold(cl_img, 0,255, cv2.THRESH_MASK)

#cv2.imshow("Original", img)
#cv2.imshow("Binary Threshold 1", thresh1)
cv2.imshow("OTSU", thresh2)
#cv2.imshow("MASK", thresh3)
cv2.waitKey(0)
cv2.destroyAllWindows()
