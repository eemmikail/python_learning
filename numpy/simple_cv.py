'''
Basit Görüntü İşleme (Parlaklık Ayarı):

Senaryo: Küçük bir siyah-beyaz görüntü, piksellerinin parlaklık değerlerini (0: siyah, 255: beyaz) içeren 5x5 boyutlu bir NumPy matrisi ile temsil ediliyor:
[[ 10,  20,  30,  40,  50],
 [ 60,  70,  80,  90, 100],
 [110, 120, 130, 140, 150],
 [160, 170, 180, 190, 200],
 [210, 220, 230, 240, 250]]
Görev: Görüntünün parlaklığını 30 birim artırın. Ancak, piksel değerlerinin 255'i geçmemesini ve 0'ın altına düşmemesini sağlayın (bu örnekte alta düşme olmaz ama genel bir kuraldır). Sonuç matrisini gösterin.
İpucu: Matris toplama işlemi, np.clip() fonksiyonu (değerleri belirli bir aralıkta sınırlamak için).
'''

import numpy as np

image_matris = np.array([[ 10,  20,  30,  40,  50],
                        [ 60,  70,  80,  90, 100],
                        [110, 120, 130, 140, 150],
                        [160, 170, 180, 190, 200],
                        [210, 220, 230, 240, 250]])

image_increase_brigtness = np.clip(image_matris + 30, 0, 255)
print(image_increase_brigtness)