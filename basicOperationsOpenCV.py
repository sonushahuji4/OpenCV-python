import numpy as np
import cv2

img=cv2.imread('images/watch.png',cv2.IMREAD_COLOR)
#print(img)
#px=img[100,100]
img[100,100]=[255,255,255]
img[200:250,200:250]=[255,255,255]
watch_face = img[50:150,100:200]
img[0:100,0:100] = watch_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/basicoperationonimage.png',img)
# px=img[100,100]
# print(px)
# ROI => Region of Image (sub image of image)