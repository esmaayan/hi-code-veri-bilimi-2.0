# Faktöriyel adında fonksiyon oluşturulur. 
# Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır.
# Format metodunu kullanılarak ekrana yazdırılır.

sayi = int(input("sayı giriniz: "))

def faktoriyel():
    faktoriyel = 1
    for i in range (sayi, 0, -1):
        faktoriyel *= i
    return faktoriyel
    
sonuc = faktoriyel()
print("{}!={}".format(sayi ,sonuc))