# Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur. 
# Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır.
import numpy as np

bir = np.array([1, 2])
iki = np.array([[3, 4], [5, 6]]) 
uc = np.array([[7, 8], [9, 10], [11, 12]])

print(bir[0])
print(iki[0:2])
print(uc[1:2])