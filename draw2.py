import cv2
import numpy

image = numpy.zeros([200,300], dtype = numpy.uint8)

center_x = 155
center_y = 100
radius = 50

cv2.circle(image, (center_x, center_y), radius, (255, 255, 255), -1)
cv2.imshow("Circle on Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()