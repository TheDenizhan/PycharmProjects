from cv2 import*
from numpy import*

image1=imread("blur.jpg")
#MEAN FİLTER
meanFilter=blur(image1,(3,3))       #3-3 bir pixel içeriisndeki sayıların
meanFilter2=blur(image1,(5,5))
meanFilter3=blur(image1,(51,51))
#medianfilter
medianFilter=medianBlur(image1,1)
#gaussFilter
gausFilter=GaussianBlur(image1,(5,5),0)
gausFilter2=GaussianBlur(image1,(5,5),-25)
gausFilter3=GaussianBlur(image1,(5,5),1000)

imshow("image",image1)
imshow("meanFilter",meanFilter)
imshow("meanFilter2",meanFilter2)
imshow("meanFilter3",meanFilter3)
imshow("Gausfilter",gausFilter)
imshow("Gausfilter2",gausFilter2)
imshow("Gausfilter3",gausFilter3)

imshow("medianFilter",medianFilter)

waitKey(0)
destroyAllWindows()