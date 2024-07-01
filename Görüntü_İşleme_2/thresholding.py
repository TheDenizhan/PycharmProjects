from cv2 import*
from numpy import*

image=imread("wp2.jpg",0)
#image=blur(image,(5,5))
#simple Thresholding
ret,thresh1=threshold(image,127,255,THRESH_BINARY)      #127 altındaysa 255 yap
#ret,thresh2=threshold(image,127,255,THRESH_BINARY_INV)  #
#ret,thresh3=threshold(image,127,255,THRESH_TRUNC)
#ret,thresh4=threshold(image,127,255,THRESH_TOZERO)
#ret,thresh5=threshold(image,127,255,THRESH_TOZERO_INV)

#adapted Thresholding
thresh6=adaptiveThreshold(image,255,ADAPTIVE_THRESH_MEAN_C,\
                          THRESH_BINARY,11,2)
thresh7=adaptiveThreshold(image,255,ADAPTIVE_THRESH_GAUSSIAN_C,\
                          THRESH_BINARY,11,2)

#OTSU THRESHOLDİNG
ret2,thresh8=threshold(image,0,255,THRESH_BINARY+THRESH_OTSU)


imshow("orji",image)
imshow("thresh1",thresh1)
#imshow("thresh2",thresh2)
#imshow("thresh3",thresh3)
#imshow("thresh4",thresh4)
#imshow("thresh5",thresh5)
imshow("thresh6",thresh6)
imshow("thresh7",thresh7)
imshow("Otsu",thresh8)

waitKey(0)
destroyAllWindows()