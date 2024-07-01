from cv2 import*
from numpy import*
import numpy as np

image4=imread("image-2.jpg")
rectangle(image4,(100,200),(600,300),[0,0,255],9)
    #rectangle fonksiyonu ile se.tiğimiz 2 nokta içerisine seçtiğimiz renk ve kalınlıkta bir dörtgen oluşturuyor


imshow("kare",image4)
waitKey(0)
destroyAllWindows()