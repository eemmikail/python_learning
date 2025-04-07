'''
Sensör Verisi Dönüşümü ve Filtreleme:

Senaryo: Bir sensörden alınan sıcaklık değerleri (Celcius) bir NumPy dizisinde tutuluyor: [22.5, 23.1, 21.8, 24.0, 25.3, 20.9, 22.7]. Bu değerleri Fahrenhayt'a (°F = °C * 9/5 + 32) çevirmeniz ve 73°F ile 77°F (dahil) arasındaki "ideal" ölçümleri filtrelemeniz gerekiyor.
Görev: Celcius dizisini Fahrenhayt dizisine dönüştürün. Ardından Fahrenhayt dizisinden sadece ideal aralıktaki değerleri içeren yeni bir dizi oluşturun.
İpucu: Element-wise (öğe bazında) aritmetik işlemler, boolean indeksleme (birden fazla koşul ile &).
'''
import numpy as np

sensor_data = np.array([22.5, 23.1, 21.8, 24.0, 25.3, 20.9, 22.7])

def C_to_F(arr):
    return arr * 9/5 + 32
'''
vectorize kullanımını hatırlamak için yaptım doğrudan kullanımda olabilirdi.
fahrenheit_data = sensor_data * 9/5 + 32
'''
vectorize_func = np.vectorize(C_to_F)
result = vectorize_func(sensor_data)
ideal_results = result[(result > 73) & (result <= 77)]

print(f"Converted Fahrenheit Data: {result}")
print(f"Ideal Measurements (73°F to 77°F): {ideal_results}")

