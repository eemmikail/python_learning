'''
Hava Durumu Kayıtları:

Senaryo: Bir haftanın (Pazartesi-Pazar) öğlen saatlerindeki sıcaklık değerleri (Celcius) şu şekildedir: [15, 17, 18, 16, 19, 20, 18].
Görev: Bu sıcaklıkları bir NumPy dizisinde saklayın. Ortalama sıcaklığı, en yüksek sıcaklığı ve sıcaklığın 17 derecenin üzerinde olduğu gün sayısını bulun.
İpucu: np.array(), np.mean(), np.max(), boolean indeksleme (örn: dizi > 17).
'''

import numpy as np

weather_records = np.array([15, 17, 18, 16, 19, 20, 18])

mean_temperature = weather_records.mean()
max_temp = weather_records.max()
greater_then_17 = weather_records[weather_records > 17].size

print(f"Mean Temperature: {mean_temperature:.2f}")
print(f"Maximum Temperature: {max_temp}")
print(f"Number of Days with Temperature Greater than 17: {greater_then_17}")
