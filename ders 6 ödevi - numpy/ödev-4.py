# Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array oluşturulur.
# Bu arrayler satır ve sütun bazında birleştirilir.
import numpy as np

sifir = np.zeros((2, 2))
bir = np.ones((2, 2))

satır = np.concatenate((sifir, bir))
sütun = np.concatenate((sifir, bir), axis = 1)

print(satır)
print(sütun)