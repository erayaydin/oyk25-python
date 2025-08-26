# gruplar = ["Iron Maiden", "Duman", "Led Zeppelin"]

"""
for deger in iterable:
    her bir deger icin burasi çalışacak
"""

"""
for calisma_numarasi in range(3):
    print(f"{calisma_numarasi} kere çalışıyorum!")
"""

"""
while durum:
    durum True ise burayı çalıştır
"""

"""
i=0
while i < 10:
    print(i)
    i+=1
"""

"""
calisma_sayisi = 0
toplam = 0
while calisma_sayisi < 100:
    calisma_sayisi += 1
    if calisma_sayisi == 50:
        break
    toplam += calisma_sayisi
print(toplam)

toplam = 0
for sayi in range(1, 101):
    if sayi == 50:
        break
    toplam += sayi
print(toplam)
"""

"""
gercek_parola = "123456"
parola = ""
while parola != gercek_parola:
    parola = input("Parola: ")
print("Giriş Yaptınız!")
"""

"""
gercek_parola = "123456"
parola_dogru_mu = False
while not parola_dogru_mu:
    parola = input("Parola: ")
    if parola == gercek_parola:
        parola_dogru_mu = True
    else:
        print("Yanlış girdiniz!")
print("Giriş Yaptınız!")
"""

"""
import random

deneme_sayisi = 0
while True:
    deneme_sayisi += 1
    zar = random.randint(1, 6)
    print(f"Zar: {zar}")
    if zar == 6:
        break
print(f"Deneme Sayısı: {deneme_sayisi}")
"""

"""
zar = random.randint(1, 6)
deneme_sayisi = 1

while zar != 6:
    zar = random.randint(1, 6)
    deneme_sayisi += 1

print(f"Deneme Sayısı: {deneme_sayisi}")
"""

# print(sum(range(1, 101)))

# toplam = 1 + 2 + 3 + 4 + .... + 100

"""
Kullanıcıdan isim, yaş ve şehir alın. Bunları bir sözlük haline getirin
Sözlüğü listeye dahil edin. Kullanıcı "bitir" yazarsa listeyi ekranda
yazın.
"""

"""
liste = []

bitir = False
while bitir:
    isim = input("İsim: ")
    yas = input("Yaş: ")
    sehir = input("Şehir: ")
    kisi = { 'isim': isim, 'yas': yas, 'sehir': sehir }
    liste.append(kisi)
    sor = input("Bitirmek ister misin? ")
    if sor == "bitir":
        bitir = True

for kisi in liste:
    print(f"{kisi['isim']}, {kisi['yas']} yaşında ve {kisi['sehir']} şehrinde yaşıyor.")

"""

oyuncular = ["Komutan Logar", "216-Robot", "Ceku", "Garavel"]

"""
bulundu_mu = False
for oyuncu in oyuncular:
    print(f"Oyuncu: {oyuncu}")
    if oyuncu == "Amir Toça":
        bulundu_mu = True
        print("Buldum seni, sen Ceku'nun babasısın!")
        break
    print("Olmadı, değiş...")

if not bulundu_mu:
    print("Ceku'nun babası bulunamadı!")
"""

"""
for oyuncu in oyuncular:
    print(f"Oyuncu: {oyuncu}")
    if oyuncu == "Amir Toça":
        print("Buldum seni, sen Ceku'nun babasısın!")
        break
    print("Olmadı, değiş...")
else:
    print("Ceku'nun babası bulunamadı!")
"""

"""
[
    {
        'isim': "Eray",
        'yas': 29,
        'sehir': "İzmir",
    },
    {
        'isim': "Mustafa",
        'yas': 30,
        'sehir': 'Kütahya',
    },
    ...
]
"""

"""
sandik = []
for esya in sandik:
    if esya == "Efsanevi Kılıç":
        print("Sonunda Buldum!")
        break
    print(f"{esya} sını istemiyorum")
else:
    print("Bu sefer de efsanevi kılıcı bulamadım :(")
"""

"""
islemler = [
    { 'tur': 'gelir', 'miktar': 100 },
    { 'tur': 'gider', 'miktar': 50 },
]

if not len(islemler):
    print("Herhangi bir işlem yapmadınız!")
else:
    for islem in islemler:
        print(islem['tur'], islem['miktar'])
"""

"""
islemler = [
    { 'tur': 'gelir', 'miktar': 100 },
    { 'tur': 'gider', 'miktar': 50 },
    { 'tur': 'gider', 'miktar': 10 },
    { 'tur': 'gider', 'miktar': 5 },
]
i = 0
while i < len(islemler):
    print(islemler[i]['tur'], islemler[i]['miktar'])
    i+=1
    if i == 6:
        break
else:
    print("While içerisinde break kullanılmadı, ben çalıştım!")

"""

"""
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}")
"""


#print("blabla", end=" ")
"""
a8 b8 c8 d8... h8
a7 b7 c7 d7... h7
...
a1 b1...       h1
"""

"""
harfler = "abcdefgh"
sayilar = range(8,0,-1)

for sayi in sayilar:
    for harf in harfler:
        print(f"{harf}{sayi}", end=" ")
    print()
"""

"""
sayilar = range(1, 6)
kareler = []
for sayi in sayilar:
    karesi = sayi*sayi
    kareler.append(karesi)
"""

"""
sayilar = range(1, 6)
kareler = [sayi*sayi for sayi in sayilar]

print(kareler)
"""

"""
sayilar = range(1, 6)
tek_sayilar = [sayi for sayi in sayilar if sayi % 2 == 1]
print(tek_sayilar)

tek_sayilar = []
for sayi in sayilar:
    if sayi % 2 == 1:
        tek_sayilar.append(sayi)
"""

"""
coords = [[0,1], [1,0], [1,1], [0,0]]
# [0,1,1,0,1,1,0,0]

locs = []
for coord in coords:
    for loc in coord:
        locs.append(loc)
"""

"""
coords = [[0,1], [1,0], [1,1], [0,0]]
# [0,1,1,0,1,1,0,0]
locs = [loc if loc == 1 else 1 for coord in coords for loc in coord]
print(locs)
"""

"""
yemekler = ["Makarna", "Patlıcan", "Köfte"]
icecekler = ["Kola", "Çay", "Ice Tea", "Kahve"]

menu = []
for yemek in yemekler:
    for icecek in icecekler:
        menu.append(f"{yemek}+{icecek}")
print(menu)

menu = [f"{yemek}+{icecek}" for yemek in yemekler for icecek in icecekler]
print(menu)
"""

"""
result = []
vec = [[1,2,3], [4,5,6], [1,2], [7,8,9], [0]]
for chunk in vec:
    if len(chunk) == 3:
        for number in chunk:
            if number % 2 == 0:
                result.append(number)
print(result)
"""

"""
vec = [[1,2,3], [4,5,6], [1,2], [7,8,9], [0]]
sonuclar = [number for chunk in vec if len(chunk) == 3 \
            for number in chunk if number % 2 == 0]
print(sonuclar)
"""

puanlar = { 'Eray': 90, 'Mustafa': 100 }

#for ogrenci in puanlar:
#    print(ogrenci)

#print(list(puanlar.items()))

"""
puanlar = { 'Eray': 90, 'Mustafa': 100 }
caliskanlar = {}
for isim, puan in puanlar.items():
    if puan > 95:
        caliskanlar[isim] = puan

caliskanlar = {isim:puan for isim, puan in puanlar.items() if puan > 95}
print(type(caliskanlar))
"""

"""
cok_buyuk_bir_aralik = range(10000000)
kare_olusturucu = (sayi*sayi for sayi in cok_buyuk_bir_aralik)
print(next(kare_olusturucu))
print(next(kare_olusturucu))
print(next(kare_olusturucu))
print(next(kare_olusturucu))
"""

kisiler = ["Eray", "Mustafa", "Ali", "Ahmet", "Veli"]
kisi_verici = (kisi for kisi in kisiler)
for kisi in kisi_verici:
    print(kisi)
