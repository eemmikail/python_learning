'''
Haftalık Harcama Takibi:

Senaryo: Bir haftanın 7 günü boyunca yaptığınız harcamaları bir listeye yazdınız: [50, 75, 30, 120, 90, 60, 40] (TL cinsinden).
Görev: Bu listeyi bir NumPy dizisine dönüştürün. Ardından NumPy fonksiyonlarını kullanarak haftalık toplam harcamanızı, günlük ortalama harcamanızı, en yüksek ve en düşük harcamayı yaptığınız günkü miktarları bulun.
İpucu: np.array(), np.sum(), np.mean(), np.max(), np.min()
'''

import numpy as np

weekly_expenditure = [50, 75, 30, 120, 90, 60, 40]
nparr = np.array(weekly_expenditure)

total = nparr.sum()
mean = nparr.mean()
minimum = nparr.min()
maximum = nparr.max()

print(f"Total Expenditure: {total}")
print(f"Average Expenditure: {mean:.2f}")
print(f"Minimum Expenditure: {minimum}")
print(f"Maximum Expenditure: {maximum}")
