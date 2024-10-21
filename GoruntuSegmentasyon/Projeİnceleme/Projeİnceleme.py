# Yapılmış 3 Projenin İncelenmesi ve Açıkamaları

    # PROJE 1 → Kmeans Kullanarak Görüntü Segmentasyonu
# Bu kod, k-means kümeleme algoritmasını kullanarak görüntü segmentasyonu gerçekleştirmektedir.

"""
import cv2
import numpy as np

img = cv2.imread("fruits.png")

#Her piksel RGB değerlerini içeren 2D diziye dönüştürülüyor.
Z = img.reshape((-1, 3)) # 3 RGB Renk kanallarını temsil eder.
print(Z.shape)

Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 10 # Görüntüyü 4 farklı renge böleceğini ifade eder.

ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)

res = center[label.flatten()] # Her pikselin, ait olduğu kümenin merkez rengiyle değiştirilmesi
res2 = res.reshape((img.shape)) # Sonucun orijinal görüntü boyutlarına yeniden şekillendirilmesi

cv2.imshow("Original Image", img)
cv2.imshow("Result", res2)
cv2.imwrite("K-Means.png", res2)

cv2.waitKey(0)

cv2.destroyAllWindows()

# Kodun çıktısı görüntüyü K-means algoritması ile 4 renge ayırmış halini gösterir. Her piksel, ait olduğu küöenin merkez rengini alarak görüntüdeki nesneleri daha belirgin hale getirir.
# Böylece, görüntüdeki meyveler ve arka plan gibi farklı alanlar daha iyi ayrılabilir.

"""

    # PROJE 2 → Grapcut ile arka plan ayırma.
# Bu kod Grapcut uygulaması ile çizilen dikdörtgenin içindeki fotoğrafın arka planını siler.

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hm.jpeg') 

assert img is not None, "file could not be read, check with os.path.exists()"

# Maske oluştur
mask = np.zeros(img.shape[:2],np.uint8)

# Ön plan ve arka plan maskeleri oluştur
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

# Ön plan ve arka plan noktalarını belirlemek için dikdörtgen
rect = (50,50,450,290)

# GrabCut algoritması
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT) # Dikdörtgen çizer

#Maskeyi düzenle
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imshow("New",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

    # PROJE 3 → Watershed Algoritması ile Nesne Segmentasyonu Örneği.
# Bu kod, Watershed algoritması ile görüntüdeki nesneleri ayırarak segmentasyon işlemi yapar.

"""

import cv2
import numpy as np


image = cv2.imread('coins.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü bulanıklaştır
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Kenar tespiti
edges = cv2.Canny(blurred, 30, 150)

# Kenarları genişletmek için dilate işlemi
dilated = cv2.dilate(edges, None, iterations=2) #iterations → işlemin kaç kez tekrarlanacağını belirtir.


# Arka plan
background = cv2.bitwise_not(dilated) # kenarları ters çevirerek arkaplan maskei oluşturur.

# Ön plan maskesi oluştur
_, markers = cv2.connectedComponents(background)

# Watershed algoritmasını uygula
markers = markers + 1  # Her bir nesneyi belirtmek için 1 ekle
markers[background == 255] = 0  # Arka planı 0 olarak ayarla

# Watershed algoritmasını uygula
cv2.watershed(image, markers)

# Sonuçları görselleştirmek için renkleri ayarla
image[markers == -1] = [0, 0, 255]  # Kenarları kırmızı yap # image[markers == -1] watershehd tarafından bulunan sınırları ifade eder.

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.imshow('Dilated Edges', dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
