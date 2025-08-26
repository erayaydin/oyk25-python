"""
Kullanıcıdan aldığınız kart bilgilerini maskeleyerek (son 4 hane hariç)
göstermeniz gerekiyor.
> Kart bilgilerini giriniz: 1234567812345678
************5678
"""
kart = input("Kart bilgilerini giriniz: ") # 1234567812345678
son_4_hane = kart[-4:] # 5678
kart_uzunluk = len(kart) # 16
yildiz_sayisi = kart_uzunluk - 4 # 12
yildizlar = "*" * yildiz_sayisi # ************
sonuc = yildizlar + son_4_hane # ************5678
print(sonuc)