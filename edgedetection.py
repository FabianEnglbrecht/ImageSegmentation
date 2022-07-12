import numpy as np
import cv2

cap = cv2.imread('Samuel_organoid_segment_thresholded.jpg')

while (1):

    # Take each cap
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(cap, cap, mask=mask)

    laplacian = cv2.Laplacian(cap, cv2.CV_64F)
    sobelx = cv2.Sobel(cap, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(cap, cv2.CV_64F, 0, 1, ksize=5)

    #cv2.imshow('Original', cap)
    cv2.imshow('Mask', mask)
    #cv2.imshow('laplacian', laplacian)
    #cv2.imshow('sobelx', sobelx)
    #cv2.imshow('sobely', sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()