# Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
# Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar.
# Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter.
# Tercihe göre kalan hak bilgisi verilir.

asıl_sifre = "esma123"

isim = input("isminizi giriniz : ")
hak = 3 

while True:
    sifre = input("sifrenizi giriniz : ")
    if sifre == asıl_sifre:
        print("Giriş yapıldı.")
        break
    else:
        hak -= 1
        print("Yanlış şifre girildi!")
        print(f"{hak} yanlış hakkınız kaldı.")
        if hak == 0:
            break