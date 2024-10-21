#Görüntü Segmentasyonu Nedir?
"""

Görüntü segmentasyonu, bir görüntüyü anlamlı parçalara ayırma işlemidir.
Amaç belirli nesneleri veya bögleleri görüntüde geri kalan kısımdan ayırmaktır.
Amaç, her bir pikselin hangi nesneye ya da kategoriye ait olduğunu belirlemektir.
Örnek: Bir fotoğrafta insanları, arabaları veya binaları tespit edip farklı bölgelere ayırabiliriz.

Segmentasyon iki ana kategoriye ayrılır.

1 → Semantik Segmentasyon : Her piksel, belirli bir sınıfa atanır. Örneğin;
Tüm arabalar bir ''araba'' etiketi altında gruplanır.
2 → Instance Segmentasyon : Benzer sınıflardaki her nesne, ayrı ayrı etiketlenir.
Aynı görüntüde birden fazla araba varsa, her biri farklı bir ''araba'' etiketi olarak ayrılır.


Segmentasyon Yöntemleri:

1. → Eşikleme(Thresholding) : Piksellerin parlaklık seviyesine göre sınıflandırma yapar.
2. → Kenar Tabanlı Yöntemler : Görüntüdeki keskin geçişleri ve kenarları bulur [Kenarlar görüntünün sınırlarını belirler].
3. → Bmkge Tabanlı Yöntemler : Piksel gruplarının benzerliklerine göre segmentasyon yapar.
3. → Makine Öğrenmesi İLe Segmentasyon : Bir diğer deyişle ''Derin Öğrenme'' denilir ve çok daha karmaşık görüntü segmentasyonu görevlerinde kullanılabilir.


Görüntü Segmentasyonunun Bazı Kullanıldığı Alanlar:
→ Tıbbi Görüntüleme [Tümör Tespiti]
→ Otonom Araçlar [Nesne Tanıma]
→ Görüntü İşleme [Yüz Tanıma, Görüntü İyileştirme]
→ Tarım, Robotik ve Endüstri, Görüntü Analizi ve Veri Görselleştirme, Sanat ve Eğlence, Güvenlik, Görüntü Yeniden Yapılandırma


Özet olarak ''Segmentasyon'' → Nesneleri ayırarak, daha detaylı analizler ve işlemler yapılabilmeye yarayan bir araçtır.


Watershed, Grabcut ve K-means → Görüntü Segmentasyonunda kullanılan yöntemlerdir. Her biri bu işlemde farklı yöntemler sunar.


Watershed Algoritma → Özellikle sınırları belirgin olmayan nesneleri segmentlemek için kullanılan bir yöntemdir.
Görüntüdeki minimum noktaları dldurarak segmentasyon yapar. Genellikle kenar tespiti ve ön işleme adımlarıyla birlikte kullanılır.

Grabcut Algoritma → Daha gelişmiş ve kullanıcı etkileşimi gerektiren bir segmentasyondur. Nesnenin kabaca sınırı belirlenir, algıritma
bu sınıra göre nesneyi ve arka planı birbirinden ayırmak için iteratif [Sürecin adım adım tekrar edilerek gerçekleştirilmesi] olarak segmentasyon yapar.

K-means Kümeleme → Algoritma görüntüdeki pikselleri renk veya yoğnuluk benzerine göre k sayıda kümeye ayırır.
Kümeler, görüntüdeki farklı nesneleri temsil eder. Benzer pikseller aynı kümeye ait olur. Bu yöntem genellikle
renk tabanlı segmentasyon için tercih edilir.

Özetle:

Watershed : Kenar bulmaya dayalı.
Grabcut : Kullanıcı etkileşimli ve olasılıklı bir model.
K-means : Piksel benzerliğine göre kümeleme.























"""