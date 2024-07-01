from cv2 import*
from numpy import*

camera=VideoCapture(0)      #parametre 0 ise kendi bilgisayarın kendi kamerasından görüntü alır
                            #parametre 1 dersek usb yada ek olarak taktığımız kaynaktan görüntü alır
                            #parametre 2 dersek dosya içersine yüklediğimiz bir videodan görüntü alır
while True:
    ret,goruntu=camera.read()   #ret yazdığımız kameranın çalışıp çalışmadığını kontrol ediyor
                                #görüntü kameradan alınan görüntülerin birleşmiş hali olucak
                                #ve son olarak camera değişkeninden aldığımız fotoları görüntü değişkenine atıyoruz

    imshow("cam",goruntu)       #imshow ile goruntu gösteriliyor

    if waitKey(1) & 0xFF == ord('q'):      #waitKey yardımıyla içine girdiğimiz parametre her bir alınan görüntünün kaç milisaniye olacağı seçiliyor
        break                               #daha sonra 0xFF ile çıkış yapmak için bir tuşa atıyoruz

camera.release()                            #daha sonra kamerayı kullanmayı bırakmasını sağlıyoruz
destroyAllWindows()