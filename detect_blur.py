#import packages
from imutils import paths
import argparse
import cv2
import numpy as np

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

thresh = 155.76
above = 0
below = 0

variations = []
floatVariations = np.array(variations, dtype = np.float32)

# loop over the input images
for imagePath in paths.list_images(args["images"]):
	# load the image, convert it to grayscale, and compute the
	# focus measure of the image using the Variance of Laplacian
	# method
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
        floatVariations = np.append(floatVariations, fm)
        if fm > 155.76:
            above += 1;
        else:
            below += 1;

print 'Variances are:'
print floatVariations
print '\n'
print 'Highest variance is: ' + str(np.amax(floatVariations))
print 'Lowest variance is: ' + str(np.amin(floatVariations))
print 'Average variance is: ' + str(np.mean(floatVariations))
print 'Standard deviation is: ' + str(np.std(floatVariations)) + '\n'
thresh = np.mean(floatVariations) + 1.96 * np.std(floatVariations)
#print 'Therefore, for 95% confidence in blurriness, we should set the threshold at 1.96 * standard deviation + mean, which is: ' + str(thresh) + '\n'
print str(float(above)/np.size(floatVariations)*100) + '% of images were good'
print str(float(below)/np.size(floatVariations)*100) + '% of images were blurry'
