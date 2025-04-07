'''
Kitap İndirim Hesaplama:

Senaryo: Bir kitapçıda farklı fiyatlara sahip 5 kitabın fiyatları [80, 120, 65, 95, 150] TL olarak verilmiştir. Tüm kitaplarda %15 indirim uygulanacaktır.
Görev: Kitap fiyatlarını içeren bir NumPy dizisi oluşturun. Her bir kitabın indirimli fiyatını hesaplayarak yeni bir dizi oluşturun.
İpucu: np.array(), temel aritmetik işlemler (çarpma, çıkarma).
'''

import numpy as np

book_prices = np.array([80, 120, 65, 95, 150, 100])
print(book_prices)
# veya doğrudan 0.85 ile çarp
book_prices_minus_values = book_prices.copy() * 0.15
print(book_prices_minus_values)
book_prices = book_prices - book_prices_minus_values
print(book_prices)