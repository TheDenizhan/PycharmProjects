from cv2 import*
from numpy import*
import numpy as np

image5=imread("image-2.jpg")
image6=imread("image3.jpg")

print(image5[300,400])      #iki resimden de seçtiğimiz koordinatlardaki renkleri alıyoruz ve ekrana yazdırıyoruz
print(image6[300,400])

imshow("toplama",image5)
imshow("toplama2",image6)

print(image5[300,400]+image6[300,400])  #iki resimden gelen renk scalelerini toplayıp ekrana yazdııyoruz

waitKey(0)
destroyAllWindows()