# Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. 
# Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
# altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)
# Ödev-3: Bir önceki örnek geliştirilir.
# Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
# Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
# Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
# Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder

kullanici_adi = input("kullanıcı adınızı giriniz: ")

while True:
    sifre = input("sifrenizi giriniz : ")

    if 5 < len(sifre) < 10:
        print("hesabiniz olusturuldu.")
        break
    else: 
        print ("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!")