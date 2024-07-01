from cv2 import*
from numpy  import*


image2=imread("image-2.jpg")
#image2[:,:,0]=30      #resme komple mavi efek uygular
#image2[:,:,1]=155      #resme komple yeşil efek uygular
#image2[:,:,2]=200       #resme komple kırmızı efek uygular
image2[150:300,100:500,2]=150      #image[yükseklik,genişlik,renk]=ton
kesit=image2[150:300,100:500]       #bu koordinatlardaki alanı alıp kesit değişkenine atar
                                    #böylelikle resimden bir kesit almış oluruz

image2[0:150,0:400]=kesit           #kesilen kesiti resmin 0:150,0:400 aralığına yapıştırdı

# imshow("kesit",kesit)

imshow("manzara",image2)
waitKey(0)
destroyAllWindows()