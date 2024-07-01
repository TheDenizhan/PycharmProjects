from numpy import*
from cv2 import*

def auto_canny(image, sigma=0.33):

    v=median(image)
    lower=int(max(0,(1.0-sigma)*v))
    upper = int(min(0, (1.0 + sigma) * v))
    edged=Canny(image,lower,upper)
    return edged

foto = imread("groot.jpg")
grayimage=cvtColor(foto,COLOR_BGR2GRAY)
blur=GaussianBlur(grayimage,(3,3),0)

wide= Canny(blur,10,220)
tight=Canny(blur,200,230)
Au=auto_canny(grayimage)

imshow("groot",foto)
imshow("blur",blur)
imshow("hepsi", hstack([wide, tight,Au]))

waitKey(0)
destroyAllWindows()
