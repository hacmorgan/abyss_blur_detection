READ ME
This is the summarised version of the information relevant to this assignment. I kept a log of my progress as I completed the assignment, LOG.txt, which is more detailed but also more descriptive of my thought processes, in case that is relevant.


KEY STEPS:
	- Looked up tutorial on blurry image detection
	- Re-familiarised myself with python I/O, string concatenation and openCV
	- Wrote code to take in the image as specified and return the variance of the laplacian of the image
	- Determined threshold value for an image to be blurry [see algorithm validation]
	- Applied this to the code.


ALGORITHM VALIDATION:
	- Calculated mean and standard deviation of variance for each set of images
	- Applied the formula for 95% confidence interval to obtain threshold value of 155.76 to pass blur detection
	- Calculated the percentage of images in each set which passed this test
Blurry data: 92% failed
	     8% passed
Good data:   20% failed
	     80% passed


ASSUMPTIONS MADE:
	- The key variable here is the threshold value, it is calculated with many similar images, but if this code is tested on a very different set of images, it could be much less accurate.


CURRENT LIMITATIONS:
	- My theoretical knowledge of blur detection is low (see line 5 of LOG.txt)


WHAT I WOULD DO WITH MORE TIME:
	- Learn more about blur detection
	- Try to apply other techniques to determine blurriness and combine them with the current algorithm to increase accuracy