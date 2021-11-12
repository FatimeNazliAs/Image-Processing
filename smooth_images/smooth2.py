import cv2
from matplotlib import pyplot as plt
import numpy as np


#blurring
img = cv2.imread("img.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal")

#ortalama bulaniklastirma

dst2 = cv2.blur(img, ksize=(3,3))
#plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("ortalama")

#gaussian blur

gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gaussian blur")

#medyan size
mb= cv2.medianBlur(img , ksize=3)
#plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("median blur")



def gaussianNose(image):
    row,col,ch = image.shape
    mean= 0
    var = 0.05
    sigma =var**0.05

    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss =gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy

#ice aktar normalize et
img = cv2.imread("img.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
#plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal1")

gaussianNoisyImage = gaussianNose(img)
#plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("gauss noisy"),plt.show()



gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize=(3,3), sigmaX=7)
#plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("with gaussian blur"),plt.show()


def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy =np.copy(image)

    #salt beyaz
    num_salt = np.ceil(amount*image.size*s_vs_p)
    coords = [np.random.randint(0, i-1,int(num_salt))for i in image.shape]
    noisy[coords] = 1

    # pepper siyah
    num_pepper = np.ceil(amount * image.size * (1-s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 1

    return noisy


spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("sp ımage"),plt.show()