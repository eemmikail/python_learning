'''
Aylık Satış Verilerini Düzenleme:

Senaryo: Bir mağazanın 3 farklı ürününün 4 haftalık satış adetleri tek bir listede sırayla verilmiştir: [10, 15, 12, 20, 18, 22, 25, 20, 8, 10, 14, 11] (Önce 1. ürünün 4 haftası, sonra 2. ürünün 4 haftası...).
Görev: Bu tek boyutlu listeyi, satırların ürünleri, sütunların haftaları temsil ettiği 3x4 boyutlu bir NumPy matrisine dönüştürün. Ardından her ürünün aylık toplam satışını ve her haftanın toplam satışını hesaplayın.
İpucu: np.array(), reshape(), sum(axis=...).
'''
import numpy as np

sales = np.array([10, 15, 12, 20, 18, 22, 25, 20, 8, 10, 14, 11])
sales = sales.reshape(3,4)
print(sales)
monthly_total = sales.sum(axis=1)
print(monthly_total)
weekly_total = sales.sum(axis =0)
print(weekly_total)

print("Monthly Sales Totals for Each Product:")
for i, total in enumerate(monthly_total, start=1):
    print(f"Product {i}: {total} units")

print("\nWeekly Sales Totals:")
for week, total in enumerate(weekly_total, start=1):
    print(f"Week {week}: {total} units")

