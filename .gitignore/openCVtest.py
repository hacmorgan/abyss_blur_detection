import numpy as np
import cv2

imageName = raw_input("Name of image: ")
concatStr = raw_input("Name of bongo: ")
print(imageName)
print(concatStr)
print(imageName+concatStr)
#load colour image as grayscale
img = cv2.imread('a.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('piccy',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
