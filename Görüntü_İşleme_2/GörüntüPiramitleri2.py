from cv2 import*
from numpy import*

image1=zeros((300,300,3),"uint8")       #zeros fonksiyonu kullanarak siyah bir resim oluşturuyoruz
                                        #zeros((yükseklik,genişlik,kanal),veritipi)
print(image1)                           #yazdırıyoruz
waitKey(0)
destroyAllWindows()