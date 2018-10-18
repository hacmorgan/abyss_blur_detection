import numpy as np
#from imutils import paths
import cv2
import argparse

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

parser = argparse.ArgumentParser(description='Image Processor')
parser.add_argument("image")
args = parser.parse_args()

#load colour image as grayscale
img = cv2.imread(args.image,cv2.IMREAD_GRAYSCALE)
fm = variance_of_laplacian(img)

if fm > 155.76:
    print 0
else:
    print 1
