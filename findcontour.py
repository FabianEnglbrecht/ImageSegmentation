import cv2
import numpy as np

img = cv2.imread('org2.png')
retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

indices = np.where(threshold==0)
threshold[indices[0], indices[1], :] = [0, 0, 255]

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()