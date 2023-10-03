# Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. 
# Kullanıcının geliri;
# 10000 ve altındaysa maaşından %5 kesinti olur.
# 25000 ve altındaysa maaşından %10 kesinti olur.
# 45000 ve altındaysa maaşından %25 kesinti olur.
# Diğer koşullarda %30 kesinti olur.

maas = int(input(" maas bilgisini giriniz: "))

if maas <= 10000:
    kesinti_10000 = maas * 0.05
    print(kesinti_10000)
elif maas <= 25000:
    kesinti_25000 = maas * 0.10
    print(kesinti_25000)
elif maas <= 45000:
    kesinti_45000 = maas * 0.25
    print(kesinti_45000)
else:
    kesinti_diğerlerine = maas * 0.30
    print(kesinti_diğerlerine)