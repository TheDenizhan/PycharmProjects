from cv2 import *
from numpy import *

image1=imread("Bitwise1.png")
image2=imread("bitwise2.png")

bit_and=bitwise_and(image1,image2)      #İki görüntüye and işlemi yapar:ikisi 1 ise 1 döner yoksa her koşul 0
bit_or=bitwise_or(image1,image2)        #iki görüntüye or işlemi yapar:işlemde 1 varsa 1 dir yoksa 0
bit_not=bitwise_not(image1)             #görüntüye not işlemi yapar:1 i 0 ,0 ı 1 yapar
bit_xor=bitwise_xor(image1,image2)      #iki görüntüye xor işlemi yapar:0,0ve 1,1 0dır, 0,1 ve 1,0 1 dir

imshow("image1",image1)
imshow("image2",image2)
imshow("bitAnd",bit_and)
imshow("bitOr",bit_or)
imshow("bitNot",bit_not)
imshow("bitXor",bit_xor)

waitKey(0)
destroyAllWindows()