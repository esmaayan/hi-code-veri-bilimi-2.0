# Ödev-5: "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.

x = "Hi-Kod Veri Bilimi Atölyesi"
# İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.
x.split()
# İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ")
x.upper()
# İfadeyi hepsini kücük harf olacak hale çevrilir.("hi-kod veri bilimi atölyesi")
x.lower()

# "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")
sayilar = "0123456789"

tek  = sayilar[0::2]
cift = sayilar[1::2]

print(tek)
print(cift)