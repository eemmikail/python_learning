'''
Stok Getiri Korelasyonu:

Senaryo: İki farklı hisse senedinin son 10 günlük kapanış fiyatları iki ayrı NumPy dizisinde bulunuyor:
Hisse A: [100, 102, 101, 105, 107, 106, 108, 110, 112, 111]
Hisse B: [50, 51, 52, 51, 53, 54, 55, 53, 56, 57]
Görev: Önce her iki hisse senedi için günlük yüzdesel getirileri ((bugünkü_fiyat - dünkü_fiyat) / dünkü_fiyat * 100) hesaplayın (ilk gün için getiri hesaplanamaz). Ardından bu iki getiri serisi arasındaki korelasyon katsayısını hesaplayın. Bu katsayı, iki hissenin fiyatlarının ne kadar birlikte hareket ettiğini gösterir.
İpucu: Dizi dilimleme, element-wise aritmetik işlemler, np.diff() (farkları almak için), np.corrcoef().
'''

import numpy as np
stock_A = np.array([100, 102, 101, 105, 107, 106, 108, 110, 112, 111])
stock_B = np.array([50, 51, 52, 51, 53, 54, 55, 53, 56, 57])

def calc_daily_return(arr):
    print("Input Array:", arr)
    
    differences = np.diff(arr)
    print("Differences (Current Price - Previous Price):", differences)
    
    old_prices = arr[:-1]
    print("Old Prices (Previous Day Prices):", old_prices)
    
    daily_returns = (differences / old_prices) * 100
    print("Daily Returns (%):", daily_returns)
    
    return daily_returns

stock_a_daily = calc_daily_return(stock_A)
stock_b_daily = calc_daily_return(stock_B)

correlation_matrix = np.corrcoef(stock_a_daily,stock_b_daily)
correlation_ab = correlation_matrix[0,1]
print(f"Correlation between Stock A and Stock B daily returns: {correlation_ab:.2f}")
