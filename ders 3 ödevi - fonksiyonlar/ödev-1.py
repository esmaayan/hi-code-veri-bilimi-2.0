# Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.
def daireAlani():
    pi = int(input("pi degerini giriniz: "))
    yaricap = int(input("yaricap degerini giriniz: "))
    return 2*pi*(yaricap**2)

print(daireAlani())