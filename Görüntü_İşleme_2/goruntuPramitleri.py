from cv2 import*
from numpy import*

image1=imread("wp34.jfif")
ikikatB=pyrUp(image1)           #resmi 2 kat büyütüyor(yükseklik*2,genişlik*2)
ikikatK=pyrDown(image1)         #resmi 2 kat küçültüyor(yükseklik/2,genişlik/2)

print("orji",image1.shape)      #resmin orjinal değerleri yazılıyor
print("ikiKB",ikikatB.shape)    #resmin 2 kat büyültülmüş değerleri yazılıyor
print("ikiKK",ikikatK.shape)    #resmin 2 kat küçültülmüş değerleri yazılıyor

imshow("orj",image1)
imshow("ikiKB",ikikatB)
imshow("ikiKk",ikikatK)

waitKey(0)
destroyAllWindows()