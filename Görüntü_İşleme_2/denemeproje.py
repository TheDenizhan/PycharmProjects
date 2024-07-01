from cv2 import*
from numpy import*

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# return the edged image
	return edged

	image1 =cv2.imread("groot.jpg",0)

	blur = GaussianBlur(imagegray, (3, 3), 0)

	wide = Canny(blur, 10, 220)
	tight = Canny(blur, 200, 230)
	auto = auto_canny(image1)

	imshow("groot", image1)
	imshow("blur", blur)
	imshow("hepsi", hstack([wide, tight, auto]))

	cv2.waitKey(0)
	destroyAllWindows()
