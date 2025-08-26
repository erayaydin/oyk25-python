"""
Ürün 1 Adı Giriniz:
Ürün 1 Tutarı Giriniz:
Ürün 2 Adı Giriniz:
Ürün 2 Tutarı Giriniz:
Ürün 3 Adı Giriniz:
Ürün 3 Tutarı Giriniz:
... (ürünler)
Toplam: ...
"""
urun1_isim = input("Ürün 1 Adı Giriniz: ")
urun1_tutar = int(input("Ürün 1 Tutar Giriniz: "))
if urun1_tutar <= 0:
    print("geçersiz bir ürün tutarı girdiniz, tekrar çalıştırınız")
else:
    urun2_isim = input("Ürün 2 Adı Giriniz: ")
    urun2_tutar = int(input("Ürün 2 Tutar Giriniz: "))
    if urun2_tutar <= 0:
        print("geçersiz bir ürün tutarı girdiniz, tekrar çalıştırınız")
    else:
        urun3_isim = input("Ürün 3 Adı Giriniz: ")
        urun3_tutar = int(input("Ürün 3 Tutar Giriniz: "))
        if urun3_tutar <= 0:
            print("geçersiz bir ürün tutarı girdiniz, tekrar çalıştırınız")
        else:
            print("== Ürünler ==")
            print(f"{urun1_isim}: {urun1_tutar}")
            print(f"{urun2_isim}: {urun2_tutar}")
            print(f"{urun3_isim}: {urun3_tutar}")
            toplam = urun1_tutar + urun2_tutar + urun3_tutar
            print(f"== Toplam: {toplam} ==")
