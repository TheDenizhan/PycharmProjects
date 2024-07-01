import cv2                               #OpenCV 'yi dosyasını yüklicek


image=cv2.imread("I.E.1.png",0)          #cv2 dosyasınından aldığımız imread fonksiyonu ile resmimizi okuyoruz
                                         #resmi yazdıktan sonra 0 koyarsanız resim renksiz biçimde yazdırılacak
cv2.imshow("Denizhan Medikal",image)     #cv2 dosyasından aldığımız imshow ile resmi gösteriyoruz
cv2.imwrite("I.E.1-Black.png",image)     #imwrite fonksiyonu ile siyaha çevirdiğimiz resmi kaydediyoruz
                                         #ilk başa resme vermek istediğimiz adı daha sonra göstermek istediğimiz resmi yazıyoruz
cv2.waitKey()                           #cv2 dosyasından aldığımız waitKey yardımıyla o resmi ekranda kalmasını sağlıyoruz
                                         #Eğer waitKey fonksiyonunun içerisine 0 yazmaz iseniz resim kaybolacaktır
cv2.destroyAllWindows()                  #destroyAllWimdows fonksiyonu sayesinde de penceremizi kapatıyoruz
print(image)                             #eğer resmi printle yazdırsak her bir pixelin aldığı değeri yazdırır
print(image.size)                        #resmin boyutunu
print(image.dtype)                       #resmin bir pikselde ne kadar yer kapladığını
print(image.shape)                       #(genişlik,yükseklik,renk)olduğunu belirtir
print(image[(78),(200)])                 #belirtiğim koordinatlardaki pikselin renk değerini bize yazdırır
