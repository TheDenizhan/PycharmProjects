from cv2 import*
from numpy import*
import numpy as np

image3=imread("image-2.jpg")
aynalama=copyMakeBorder(image3,500,500,500,500,BORDER_REFLECT)  #aynalama efekti

uzatma=copyMakeBorder(image3,100,100,100,100,BORDER_REPLICATE)  #uzaatma efekti

tekrarlama=copyMakeBorder(image3,100,100,100,100,BORDER_WRAP)    #tekrarlama efekti

cerceve=copyMakeBorder(image3,100,100,100,100,BORDER_CONSTANT,value=(70,120,255))   #çerçeve oluşturma efekti
    #eğer son value değeri girilmez ise çerçeveyi siyah yazdırır

imshow("aynalama",aynalama)
imshow("uzatma",uzatma)
imshow("tekrar",tekrarlama)
imshow("border",cerceve)

waitKey(0)
destroyAllWindows()
