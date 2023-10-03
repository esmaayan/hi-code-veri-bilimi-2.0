# Sayılardan oluşan bir boyutlu array oluşturulur.
# Arrayi oluştururken sayıların veri tipini integer olarak belirtilir. 
# Oluşturulan arrayin boyut, eleman sayısı bilgilerine bakılır.
import numpy as np

array1 = np.array([1, 2, 3, 4], dtype = int)
array1_ndim = array1.ndim
array1_size = array1.size

print(array1_ndim)
print(array1_size)