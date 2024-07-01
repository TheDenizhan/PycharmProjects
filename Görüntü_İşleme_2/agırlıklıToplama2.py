from cv2 import*
from numpy import*
import numpy as np
#iki resim aynı boyutta olmak zorunda
image10=imread("wp4.jpg")
image11=imread("wp2.jpg")


imshow("wp1",image10)
imshow("wp2",image11)


toplam=add(image10,image11)     #bir değişkene birleştirip 2 resmi atıyoruz
toplam2=addWeighted(image10,0.9,image11,0.1,0)  #2 resim değişkenlerinin birleştiklerinde ki oranı yazıyoruz
imshow("toplam2",toplam2)
imshow("toplama",toplam)
waitKey(0)
destroyAllWindows()