# Enumerate method araştırılır ve belirlenen örnek enumerate metodu ile yapılır.
# for index in range(len(meyveler)):
#     print("{}. indexte bulunan meyve: {}".format(index,meyveler[index]))
# Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

meyveler = ["elma", "muz", "portakal", "ayva", "mandalina"]

for index, meyve in enumerate(meyveler):
    print("{}. indexte bulunan meyvenin adı : {}".format(index , meyve))

yeni_liste = [meyveler for meyve in meyveler if str in meyve]
print(yeni_liste)