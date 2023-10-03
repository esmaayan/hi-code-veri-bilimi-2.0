# Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik,Fizik,Kimya notları tutulur.
# Kullanıcıdan isim ve ders ismi(Matematik,Fizik,Kimya) istenir ve bu bilgilere göre çıktı verilir.

ogrenci_notlari = {}

isim = input("isminizi giriniz : ")
ders = input("dersi seçiniz (matematik/fizik/kimya): ")
ogrenci_not = input("notunuzu giriniz: ")

ogrenci_notlari[isim] = {ders : ogrenci_not}
print(f"{isim} adlı öğrencinin {ders} notu: {ogrenci_notlari[isim][ders]}")