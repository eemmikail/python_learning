'''
Müşteri Konumlarına Göre Mesafe Hesabı:

Senaryo: 3 müşterinin bir harita üzerindeki (x, y) koordinatları bir NumPy matrisinde tutuluyor: [[10, 20], [15, 35], [5, 25]]. Şirketinizin merkezi ise [0, 0] noktasındadır.
Görev: Her bir müşterinin şirketinize olan Öklid mesafesini (sqrt((x2-x1)^2 + (y2-y1)^2)) hesaplayın ve mesafeleri içeren bir dizi oluşturun. En yakın ve en uzak müşteriyi bulun.
İpucu: Matris indeksleme/dilimleme, np.sqrt(), np.sum(axis=1), np.argmin(), np.argmax(). Broadcasting (yayma) özelliğini kullanmak da işleri kolaylaştırabilir.
'''
import numpy as np

customer_locations = np.array([[10, 20], [15, 35], [5, 25]])
company_center = np.array([0,0])

def euclid(loc1, loc2):
    '''
    Alternatif olarak linalg.norm kullanılabilir.
    np.linalg.norm(vec1 - vec2)
    '''
    return np.sqrt(np.sum((loc1 - loc2) ** 2))

distances = np.array([euclid(location, company_center) for location in customer_locations])
'''
#veya aşağıdaki yöntem numpy ile olduğu için daha verimli.
# Broadcasting ile merkez noktasını her müşteri konumundan çıkarma
# customer_locations (3, 2) - company_center (2,) -> (3, 2)
differences = customer_locations - company_center

# Farkların karesini alma (element-wise)
squared_diffs = differences ** 2 # Shape: (3, 2)

# Karelerin toplamını satır bazında (axis=1) alma (x^2 + y^2)
sum_squared_diffs = np.sum(squared_diffs, axis=1) # Shape: (3,)

# Karekök alarak Öklid mesafelerini bulma
distances_broadcast = np.sqrt(sum_squared_diffs) # Shape: (3,)
'''

closest_customer_index = np.argmin(distances)
farthest_customer_index = np.argmax(distances)

print(f"Distances from Company Center: {distances}")
print(f"Closest Customer Index: {closest_customer_index}, Distance: {distances[closest_customer_index]}")
print(f"Farthest Customer Index: {farthest_customer_index}, Distance: {distances[farthest_customer_index]}")
