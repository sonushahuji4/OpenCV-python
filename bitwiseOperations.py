import cv2
import numpy as np

# Load two images
img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainlogo.png')

# put a logo on top left corner
rows,cols, channels = img2.shape
roi = img1[0:rows,0:cols]

# Create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)    # converts the logo to gray color
# cv2.imshow('img2gray',img2gray)

# add threshold
ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)   # converts the background in black and portion of the image in white
mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv',mask_inv)

# black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# cv2.imshow('img1_bg',img1_bg)

img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/img.png',img1)