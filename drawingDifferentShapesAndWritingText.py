import numpy as np
import cv2

img=cv2.imread('images/watch.png',cv2.IMREAD_COLOR)
'''
# Drawing a line on the image using cv2
# cv2.line('draw line on the image','from where does the line starts','where does the line ends','color of the line(BGR)','line width')
'''
# -----------------NOTE------------------
# Blue => (255,0,0)
# Green => (0,255,0)
# Red => (0,0,255)
# Black => (0,0,0)
# White => (255,255,255)
'''

cv2.line(img,(60,10),(60,100),(255,0,0),15)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/line.png',img)

# output is in directory "output" =.line.png
'''

# Drawing a rectange on the image using cv2
# cv2.reactangle(image,start from(x,y),end at(x,y),color,thickness)

# cv2.rectangle(img,(20,400),(340,100),(0,255,0),5)
# cv2.imshow('rectangle',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('output/line.png',img)
# cv2.imwrite('output/reactangle.png',img)

# cv2.circle(image,start from(x,y),radius,color,thickness)
cv2.circle(img,(175,245),140,(0,0,255),5)
cv2.imshow('rectangle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/line.png',img)
cv2.imwrite('output/circle.png',img)