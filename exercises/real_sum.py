"""
Kullanıcıdan tek input ile sayı listesi alacağız. Kullanıcı sayıları
boşluk ile ayıracak. Sayı olmayanları dahil etmeden toplamını
hesaplayacağız.
> Sayılar: 12 1 8 99 aa u 3
Toplam: 123
"""

girilen = input("Sayılar: ")
sayilar = girilen.split()

"""
sayilar = girilen.split()
toplam = 0
for sayi in sayilar:
    if sayi.isdigit():
        toplam += int(sayi)
print(f"Toplam: {toplam}")
"""

sayi_olanlar = [int(sayi) for sayi in sayilar if sayi.isdigit()]
toplam = sum(sayi_olanlar)
print(toplam)