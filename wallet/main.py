"""
Cüzdan programımızda işlemleri şimdilik bellekte tutacağız.
Bunun için bir işlem listesi oluşturunuz. Kullanıcıya yapmak
istediği işlemi sorunuz:
- (e)kleme
- (l)isteleme
- (b)akiye
- (c)ikis
Kullanıcı 'çıkış' işlemi haricinde tekrar bu menüye dönmeli.
Ekleme işlemi yapmak istediği durumda:
  - Kullanıcıdan tarih (Yıl-Ay-Gün şeklinde: "2025-08-25") bilgisi alın.
  - Kullanıcıdan işlem adı bilgisi alın.
  - Kullanıcıdan tür ('giren' yada 'çıkan') bilgisi alın.
  - Kullanıcıdan miktar (ondalıklı) bilgisi alın.
  - Kullanıcıdan kategori (boş karakter gelirse None) bilgisi alın.
  - Bu değerleri 1 tuple içerisinde birleştirip işlemler listesine ekleyin.
  Örnek tuple: ("2025-08-25", "Kola aldım, yay!", "çıkan", "Market", 70)
  Örnek tuple: ("2025-08-01", "Kredi kartlarımın maaşı yatmış", "giren", "Maaş", 10000)
Listeleme işlemi yapmak istediği durumda:
  - işlemler listesini ekrana yazmalı (nasıl görüneceği size kalmış)
Bakiye işlemi yapmak istediği durumda:
  - İşlemlerin hepsi toplanmalı ve kullanıcıya gösterilmeli.
  ! İşlemin türüne dikkat, eğer çıkan ise net miktar eksi olmalı
BONUS: Menüye - (r)apor maddesi ekleyin ve kullanıcıdan Yıl-Ay bilgisi isteyin.
Bu Yıl-Ay tarihine ait işlemler listelenmeli ve toplamı yazmalı.
"""

islemler = []
menu = ""
while menu != "c":
    menu = input("(e)kleme, (l)isteleme, (b)akiye, (r)apor, (c)ikis: ")
    if menu == 'e':
        print("Ekleme işlemi yapalım...")
        tarih = input("Tarih (Yıl-Ay-Gün): ")
        adi = input("İşlem Adı: ")
        tur = ""
        while tur != 'giren' and tur != 'cikan':
            tur = input("İşlem Türü (giren/cikan): ")
        miktar = float(input("Tutar: "))
        kategori = input("Kategori: ")
        if kategori == "":
            kategori = None
        islem = (tarih, adi, tur, miktar, kategori)
        islemler.append(islem)
    elif menu == 'l':
        for tarih, adi, tur, miktar, kategori in islemler:
            print(f"{tarih}'inde {adi} işlemi yaptınız. Türü: {tur} Miktar: {miktar} Kategori: {kategori}")
    elif menu == 'b':
        bakiye = 0
        for islem in islemler:
            if islem[2] == 'giren':
                bakiye += islem[3]
            else:
                bakiye -= islem[3]
        print(f"Bakiye: {bakiye}")
    elif menu == 'r':
        istenen = input("Yıl-Ay bilgisi giriniz: ")
        toplam = 0
        for tarih, adi, tur, miktar, kategori in islemler:
            if tarih[0:7] == istenen:
                if tur == 'giren':
                    toplam += miktar
                else:
                    toplam -= miktar
                print(f"{tarih}'inde {adi} işlemi yaptınız. Türü: {tur} Miktar: {miktar} Kategori: {kategori}")
        print(f"Toplam: {toplam}")

print("Programım bitti!")
