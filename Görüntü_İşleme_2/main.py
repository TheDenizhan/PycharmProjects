from cv2 import*
from numpy  import*

image=imread("image-2.jpg")
image[50,30]=[255,255,255]          #seçtiğimiz kordinatlara seçtiğimiz renkte bir nokta oluşturuyor
for i in range(100):                #bir döngü içerisine veridiğimiz 100 değeri ile çizgi oluşturuyoruz
    image[100,i] = [255, 255, 255]  #
    for i in range(100):
        image[i, 100] = [255, 255, 255]
imshow("Manzara",image)
waitKey(0)
destroyAllWindows()
