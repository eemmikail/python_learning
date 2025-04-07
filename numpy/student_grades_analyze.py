'''
Öğrenci Not Analizi:

Senaryo: Bir sınıftaki 10 öğrencinin bir sınavdan aldığı notlar: [65, 72, 88, 55, 91, 72, 80, 45, 95, 77]. Geçme notu 70'tir.
Görev: Notları bir NumPy dizisine aktarın. Sınavı geçen öğrenci sayısını, kalan öğrenci sayısını ve sınıfın not ortalamasını hesaplayın. Ayrıca 90 ve üzeri alan "başarılı" öğrencilerin notlarını ayrı bir dizi olarak gösterin.
İpucu: np.array(), boolean indeksleme, np.sum() (boolean dizide True'ları saymak için), len(), np.mean().
'''

import numpy as np

grades = np.array([65, 72, 88, 55, 91, 72, 80, 45, 95, 77])
number_of_pass = (grades >= 70).sum()
number_of_fail = (grades < 70).sum()
mean = grades.mean()
successful_students = grades[grades >= 90]

print(f"Number of Students Passed: {number_of_pass}")
print(f"Number of Students Failed: {number_of_fail}")
print(f"Class Average: {mean:.2f}")
print(f"Successful Students' Grades (90 and above): {successful_students}")


