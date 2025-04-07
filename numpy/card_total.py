'''
Alışveriş Sepeti Toplam Maliyeti:

Senaryo: Bir market alışverişinde alınan ürünlerin miktarları (adet veya kg) ve birim fiyatları (TL) iki ayrı NumPy dizisinde tutuluyor:
Miktarlar: [2, 0.5, 3, 1, 5] (örn: 2 adet ekmek, 0.5 kg peynir, 3 litre süt, 1 paket makarna, 5 adet yumurta)
Birim Fiyatlar: [7.5, 80, 25, 15, 2.5] (örn: Ekmek 7.5 TL/adet, Peynir 80 TL/kg, Süt 25 TL/litre...)
Görev: NumPy'nin vektörel çarpım özelliğini kullanarak her bir ürün grubu için ödenecek tutarı hesaplayan bir dizi ve ardından alışveriş sepetinin toplam maliyetini bulun.
İpucu: np.multiply() veya * (element-wise çarpım), np.sum(). Alternatif olarak doğrudan np.dot() (nokta çarpım) da kullanılabilir.
'''

import numpy as np

quantities = np.array([2, 0.5, 3, 1, 5])
unit_prices = np.array([7.5, 80, 25, 15, 2.5])
costs = quantities*unit_prices
total_cost = costs.sum()

print(f"Costs for Each Product: {costs}")
print(f"Total Cost of Shopping Cart: {total_cost:.2f} TL")
