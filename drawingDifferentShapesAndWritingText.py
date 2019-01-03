import numpy as np
import cv2

img=cv2.imread('images/watch.jpg',cv2.IMREAD_COLOR)

# Drawing a line on the image using cv2
# cv2.line('draw line on the image','from where does the line starts','where does the line ends','color of the line(BGR)','line width')
'''
-----------------NOTE------------------
Blue => (255,0,0)
Green => (0,255,0)
Red => (0,0,255)
Black => (0,0,0)
White => (255,255,255)
'''

cv2.line(img,(60,10),(60,100),(255,0,0),15)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/line.png',img)

# output is in directory "output" =.line.png