'''
Müşteri Konumlarına Göre Mesafe Hesabı:

Senaryo: 3 müşterinin bir harita üzerindeki (x, y) koordinatları bir NumPy matrisinde tutuluyor: [[10, 20], [15, 35], [5, 25]]. Şirketinizin merkezi ise [0, 0] noktasındadır.
Görev: Her bir müşterinin şirketinize olan Öklid mesafesini (sqrt((x2-x1)^2 + (y2-y1)^2)) hesaplayın ve mesafeleri içeren bir dizi oluşturun. En yakın ve en uzak müşteriyi bulun.
İpucu: Matris indeksleme/dilimleme, np.sqrt(), np.sum(axis=1), np.argmin(), np.argmax(). Broadcasting (yayma) özelliğini kullanmak da işleri kolaylaştırabilir.
'''

