"""
Minik minicik kütüphane otomasyonu

############
# Ana Menü #
############
İşlem seçiniz:
1) Kitap Listesi
2) Kitap Ekle
3) Kitap Çıkar
4) Kitap Ara
5) Öğrenci Listesi
6) Öğrenci Ekle
7) Öğrenci Sil
8) Öğrenci Ara
9) Kitap Emanet Et
10) Çıkış
> 1

#################
# Kitap Listesi #
#################
Kitaplar (çıkmak için q):
1) Otostopçunun Galaksi Rehberi
2) ...
> q

############
# Ana Menü #
############
İşlem seçiniz:
1) Kitap Listesi
2) Kitap Ekle
3) Kitap Çıkar
4) Kitap Ara
5) Öğrenci Listesi
6) Öğrenci Ekle
7) Öğrenci Sil
8) Öğrenci Ara
9) Kitap Emanet Et
10) Çıkış
> 2

##############
# Kitap Ekle #
############## 
Kitap Adı: Arsen Lupen - Kibar Hırsız
Sayfa: 120
Kitap eklendi! Ana menüye dönülüyor...

############
# Ana Menü #
############
İşlem seçiniz:
1) Kitap Listesi
2) Kitap Ekle
3) Kitap Çıkar
4) Kitap Ara
5) Öğrenci Listesi
6) Öğrenci Ekle
7) Öğrenci Sil
8) Öğrenci Ara
9) Kitap Emanet Et
10) Çıkış
> 9

###################
# Kitap Emanet Et #
###################
Kişi: Mustafa Yağcı
Kitap: Otostopçunun Galaksi Rehberi
Kitap ve öğrenci güncellendi! Ana menüye dönülüyor...

############
# Ana Menü #
############
İşlem seçiniz:
1) Kitap Listesi
2) Kitap Ekle
3) Kitap Çıkar
4) Kitap Ara
5) Öğrenci Listesi
6) Öğrenci Ekle
7) Öğrenci Sil
8) Öğrenci Ara
9) Kitap Emanet Et
10) Çıkış
>
"""
import kitaplar
import ogrenciler
import komut

def kitap_listesi():
    komut.baslik("Kitap Listesi")
    if len(kitaplar.kitaplar) == 0:
        print("Henüz hiç kitap kaydedilmedi")
        return

    for i, kitap in enumerate(list(kitaplar.kitaplar.keys()), start=1):
        print(f"{i}) {kitap}")

def kitap_ekle():
    komut.baslik("Kitap Ekle")
    isim = input("Kitap İsmi: ")
    if isim in kitaplar.kitaplar:
        print("Bu kitap zaten var, ana menüye döndürülüyor...")
        return
    sayfa = input("Sayfa Sayısı:")
    if sayfa != "" and not sayfa.isdigit():
        print("Sadece sayı girebilirsiniz.")
        return
    sayfa = None if sayfa == "" else int(sayfa)
    kitaplar.kitap_ekle(isim, sayfa)

def kitap_cikar():
    komut.baslik("Kitap Çıkar")
    kitap = input("Kitap Adı: ")
    islem = kitaplar.kitap_sil(kitap)
    if islem:
        print("Kitap silindi!")
    else:
        print("Bu kitap bulunamadı.")

def kitap_ara():
    komut.baslik("Kitap Arama")
    kitap_adi = input("Kitap Adı: ")
    kitap = kitaplar.kitap_ara(kitap_adi)
    if not kitap:
        print("Kitap bulunamadı.")
        return
    
    print(f"Sayfa: {kitap['sayfa'] if kitap['sayfa'] else "-"}")
    print(f"Öğrenci: {kitap['ogrenci'] if kitap['ogrenci'] else "-"}")

def ogrenci_listesi():
    komut.baslik("Öğrenci Listesi")
    if len(ogrenciler.ogrenciler) == 0:
        print("Henüz hiç öğrenci kaydedilmedi")
        return

    for i, ogrenci in enumerate(list(ogrenciler.ogrenciler.keys()), start=1):
        print(f"{i}) {ogrenci}")

def ogrenci_ekle():
    komut.baslik("Öğrenci Ekle")
    isim = input("Öğrenci İsmi: ")
    if ogrenciler.ogrenci_ara(isim):
        print("Öğrenci zaten var!")
        return
    sinif = input("Sınıf: ")
    ogrenciler.ogrenci_ekle(isim, sinif)
    print(f"{isim} öğrencisi başarıyla kaydedildi!")

def ogrenci_sil():
    komut.baslik("Öğrenci Sil")
    ogrenci_adi = input("Öğrenci Adı: ")
    islem = ogrenciler.ogrenci_sil(ogrenci_adi)
    if islem:
        print("Öğrenci silindi!")
    else:
        print("Bu öğrenci bulunamadı.")

def ogrenci_ara():
    komut.baslik("Öğrenci Arama")

    ogrenci_adi = input("Öğrenci Adı: ")
    ogrenci = ogrenciler.ogrenci_ara(ogrenci_adi)
    if not ogrenci:
        print("Öğrenci bulunamadı.")
        return
    
    print(f"Sınıf: {ogrenci['sinif']}")
    print(f"Aldığı Kitap: {ogrenci['kitap'] if ogrenci['kitap'] else "-"}")

def emanet():
    komut.baslik("Kitap Emanet Et")
    kitap_ismi = input("Kitap İsmi: ")
    if kitap_ismi not in kitaplar.kitaplar:
        print("Kitap bulunamadı, ana menüye döndürülüyor...")
        return
    kitap = kitaplar.kitap_ara(kitap_ismi)
    ogrenci_ismi = input("Öğrenci İsmi: ")
    if ogrenci_ismi not in ogrenciler.ogrenciler:
        print("Öğrenci bulunamadı, ana menüye döndürülüyor...")
        return
    ogrenci = ogrenciler.ogrenci_ara(ogrenci_ismi)
    secim = input("(T)eslim, (V)er: ")
    if secim == 'V':
        if kitap['ogrenci']:
            print("Bu kitap zaten bir öğrencide!")
            return
        if ogrenci['kitap']:
            print("Bu öğrencinin zaten bir kitabı var. Yenisini alamaz!")
            return
        kitaplar.kitap_emanet(kitap_ismi, ogrenci_ismi)
        ogrenciler.ogrenci_kitap_ekle(ogrenci_ismi, kitap_ismi)
    elif secim == 'T':
        if not kitap['ogrenci'] or kitap['ogrenci'] != ogrenci_ismi:
            print("İlgili kitap bu öğrencide değil")
            return
        if not ogrenci['kitap'] or ogrenci['kitap'] != kitap_ismi:
            print("Bu öğrenci bu kitabı almamış.")
            return
        kitaplar.kitap_emanet(kitap_ismi, None)
        ogrenciler.ogrenci_kitap_sil(ogrenci_ismi)

menu = {
    "kitap_listesi": "Kitap Listesi",
    "kitap_ekle": "Kitap Ekle",
    "kitap_cikar": "Kitap Çıkar",
    "kitap_ara": "Kitap Ara",
    "ogrenci_listesi": "Öğrenci Listesi",
    "ogrenci_ekle": "Öğrenci Ekle",
    "ogrenci_sil": "Öğrenci Sil",
    "ogrenci_ara": "Öğrenci Ara",
    "emanet": "Kitap Emanet Et",
    "cikis": "Çıkış"
}

islemler = {
    "kitap_listesi": kitap_listesi,
    "kitap_ekle": kitap_ekle,
    "kitap_cikar": kitap_cikar,
    "kitap_ara": kitap_ara,
    "ogrenci_listesi": ogrenci_listesi,
    "ogrenci_ekle": ogrenci_ekle,
    "ogrenci_sil": ogrenci_sil,
    "ogrenci_ara": ogrenci_ara,
    "emanet": emanet,
}

while True:
    komut.baslik("Ana Menü")
    secim = komut.listele_secim_al(menu)
    if secim == 'cikis':
        print("Görüşürüz!")
        break
    islemler[secim]()
