import cv2
import numpy as np

img=cv2.imread('images/bookpage.jpg')
#   step 1:
cv2.imshow('original',img)  # displaying the original image
#   step 2:
retval, threshold = cv2.threshold(img,12, 255,cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold)   # applying the threshold function of openCV

#   step 3: Converting the image to gray color
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscaled',grayscaled)
#   step 4:
ret2, threshold2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
cv2.imshow('threshold2',threshold2)
#   step 5:
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
cv2.imshow('gaus',gaus)



cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/original.jpg',img)
cv2.imwrite('output/threshold.jpg',threshold)
cv2.imwrite('output/grayscaled.jpg',grayscaled)
cv2.imwrite('output/threshold2.jpg',threshold2)
cv2.imwrite('output/gaus.jpg',gaus)