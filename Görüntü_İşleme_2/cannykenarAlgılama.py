from cv2 import *
from numpy import *

def auto_canny(blur,sigma=0.33):

    v=median(blur)
    lower=int(max(0,(1.0-sigma)*v))
    upper =int(min(255,(1.0+sigma)*v))
    edged=cv2.Canny(blur,lower,upper)

    return edged;

image1 = imread("groot.jpg")
imagegray = cvtColor(image1, COLOR_BGR2GRAY)
blur = GaussianBlur(imagegray, (3, 3), 0)


canny=Canny(blur,100,1)




wide = Canny(blur, 10, 220)
tight = Canny(blur, 200, 230)
auto = auto_canny(blur)

imshow("groot", image1)
imshow("blur", blur)
imshow("canny",canny)

imshow("hepsi", hstack([wide, tight,canny,auto]))

waitKey(0)
destroyAllWindows()
