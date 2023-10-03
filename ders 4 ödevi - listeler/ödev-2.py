# Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
yeni_liste = []

for i in liste:
    if isinstance(i, str): # isinstance(kontrol etmek istediğin değer, kontrol etmek istediğin type)
        yeni_liste.append(i)

print(yeni_liste)