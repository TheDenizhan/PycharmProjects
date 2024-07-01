from cv2 import*
from numpy import*
import numpy as np

image1=imread("wp4.jpg")
imagegray=cvtColor(image1,COLOR_BGRA2GRAY)      #resmi grileştiriyoruz

yukseklik,genislik,kanalsayisi=image1.shape     #image1 değişkeninin boyutlarını değişkenlere atıyoruz
yukseklik,genislik=imagegray.shape

print("orjinal",yukseklik,genislik,kanalsayisi)
print("gray",yukseklik,genislik)

imshow("orji",image1)
imshow("gray",imagegray)

waitKey(0)
destroyAllWindows()