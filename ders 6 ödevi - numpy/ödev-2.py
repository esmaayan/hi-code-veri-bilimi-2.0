# İki ve üç boyutlu arrayler oluşturulur. 
# Bu arraylerin boyut, eleman sayısı, satır, sütun bilgilerine ulaşılır. 
# Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır.
import numpy as np

iki = np.array([[1, 2, 3], [4, 5, 6]])
uc  = np.array([[7, 8], [9, 10], [11, 12]])

# boyut .ndim
# eleman sayısı .size
# satır, sütun .shape

iki_boyut = iki.ndim
uc_boyut  = uc.ndim
print(iki_boyut)
print(uc_boyut)

iki_elemanSayisi = iki.size
uc_elemanSayisi   = uc.size
print(iki_elemanSayisi)
print(uc_elemanSayisi)

satırİki, sütunİki = iki.shape
satırUc , sütunUc    = uc.shape
print((satırİki, sütunİki)) 
print((satırUc , sütunUc ))

print(iki[1])
print(uc[0:2])