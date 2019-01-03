import numpy as np
import cv2

img=cv2.imread('images/watch.png',cv2.IMREAD_COLOR)
# '''
# # Drawing a line on the image using cv2
# # cv2.line('draw line on the image','from where does the line starts','where does the line ends','color of the line(BGR)','line width')
# '''
# # -----------------NOTE------------------
# # Blue => (255,0,0)
# # Green => (0,255,0)
# # Red => (0,0,255)
# # Black => (0,0,0)
# # White => (255,255,255)
#
# cv2.line(img,(60,10),(60,100),(255,0,0),15)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('output/line.png',img)
#
# # output is in directory "output" =.line.png
#
#
# # Drawing a rectange on the image using cv2
# # cv2.reactangle(image,start from(x,y),end at(x,y),color,thickness)
#
# cv2.rectangle(img,(20,400),(340,100),(0,255,0),5)
# cv2.imshow('rectangle',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('output/line.png',img)
# cv2.imwrite('output/reactangle.png',img)
#
# # cv2.circle(image,start from(x,y),radius,color,thickness)
# cv2.circle(img,(175,245),140,(0,0,255),5)
# cv2.imshow('rectangle',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('output/line.png',img)
# cv2.imwrite('output/circle.png',img)

# pts = np.array([[10,5],[20,30],[70,20],[50,20]],np.int32)
# #pts = pts.reshape(img)
# cv2.polylines(img,[pts],True,(0,0,0),3)
# cv2.imshow('Poly Shape',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('output/polyshape.png',img)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Watch',(0,530),font,1,(200,25,255),5,cv2.LINE_AA)

cv2.line(img,(60,10),(60,100),(255,0,0),15)
cv2.imshow('Frame',img)

cv2.rectangle(img,(20,400),(340,100),(0,255,0),5)
cv2.imshow('Frame',img)

cv2.circle(img,(175,245),140,(0,0,255),5)
cv2.imshow('Frame',img)

pts = np.array([[10,5],[20,30],[70,20],[50,20]],np.int32)
cv2.polylines(img,[pts],True,(0,0,0),3)

cv2.imshow('Frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/final.png',img)
