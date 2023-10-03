# Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

# Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
# (Kişi 65 yaşında ise emekli olur.) 
# Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
# (Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) 
# Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 
# 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.

def yasVeEmeklilik(dogumYili, isim):
    def yas():
        return int(2023 - dogumYili)
    
    def emeklilik():
        if yas() >= 65:
            return "emekli oldunuz"
        else:
            return f"{isim} emekliliğine {65 - yas()} sene kaldı."

    yas_sonuc = yas()
    emeklilik_sonuc = emeklilik()

    return (f"{yas_sonuc} yasindasin ve {emeklilik_sonuc}")

print(yasVeEmeklilik(2003, "esma"))