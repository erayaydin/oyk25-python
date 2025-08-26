"""
Kupon doğrulama sistemi yapacağız. Kullanıcı kupon bilgisini girecek.
Bu bilgi 8 haneli olmalı ve son 2 hanesi sayı olmalıdır. Geçerli bir
kupon ise ekrana "Geçerli kupon kullanıldı!" yazıp başa dönmeli
(çıkış yazana kadar). Geçerli olan kuponları bir yerde kaydederek
aynı kupon kullanıldığında "Bu kupon kullanıldı" yazmalıdır.
> Kupon: abcdef01
Geçerli kupon kullanıldı!
> Kupon: ab0defgh
Geçersiz kupon!
> Kupon: abcdef01
Bu kupon kullanıldı!
> Kupon: cikis
Bye bye!
"""
kullanilan_kuponlar = []
while True:
    kupon = input("Kupon: ")

    if kupon == "cikis":
        print("Çıkış yapılıyor...")
        break

    if len(kupon) == 8 and kupon[-2:].isdigit():
        if kupon in kullanilan_kuponlar:
            print("Bu kupon kullanıldı")
        else:
            kullanilan_kuponlar.append(kupon)
            print("Geçerli kupon kullanıldı!")
    else:
        print("Geçersiz kupon")