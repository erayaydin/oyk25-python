#
"""
metin1 = input("Bir metin gir: ")
metin2 = input("Aynısını gir: ")

print(metin1 != metin2)
"""
"""
sayi = 10
tahmin = int(input("Tahmin et: "))

print(0 < tahmin < 10)
"""

"""
yas = int(input("Yaş: "))
print(yas < 8 or yas > 60)
"""

"""
if koşul1:
    koşul1 olduğunda yapılacaklar..
elif koşul2:
    koşul1 olmadığında, koşul2 olduğunda yapılacaklar...
elif koşul3
    koşul1, koşul2 olmadığında, koşul3 olduğunda yapılacaklar...
...
else:
    hiçbir koşul uymadığında yapılacaklar...
"""

"""
print("Merhaba")
yas = int(input("Yaş: "))
if yas > 18:
    print("Bu kişinin yaşı 18'den büyükmüş")
    print("Konsere gelebilirsin!")
else:
    print("Bu kişinin yaşı 18'den büyük değilmiş; yani 18 de olabilir 18 den küçük de olabilir.")
    if yas == 18:
        print("yaşı 18'miş")
        print("Konsere giremezsin, 18 yaşındasın ama banane")
    else:
        print("yaşı 18 dışında bir şeymiş")
        print("Konsere giremezsin")
    print("kontrollerim bitti")
print("Güle güle!")
"""

"""
print("Merhaba")
yas = int(input("Yaş: "))
if yas > 18:
    print("Konsere gelebilirsin!")
elif yas == 18:
    print("Konsere giremezsin, 18 yaşındasın ama banane")
else:
    print("Konsere giremezsin")
print("Güle güle!")
"""

"""
sehirler = ["izmir", "istanbul", "ankara"]
sehir = input("Şehir gir: ")
if sehir.lower() not in sehirler:
    print("Şehir geçersiz")
else:
    print(f"{sehir} seyahat edebilirsiniz")
"""

"""
parola = input("Parola: ")
sayilardan_mi_olusuyor = parola.isdigit()

if sayilardan_mi_olusuyor:
    print("Parolanız sadece sayılar olamaz!")
else:
    print("Parolan güzel!")
"""



"""
dosyalar = ["file1.txt", "file2.txt", "file3.txt"]
"file1.txt,file2.txt,file3.txt"
print(f"{dosyalar[0]},{dosyalar[1]},{dosyalar[2]}")

dosyalar_listesi = ",".join(dosyalar)
print(dosyalar_listesi)
"""

import random
"""
x sayısı = 10
y sayısı = 5
x sayısı y sayısından büyük
"""

x = random.randint(0, 10)
y = random.randint(0, 10)

if x > y:
    print(f"x={x} sayısı {y=} den büyük")
elif x == y:
    print(f"{x=} sayısı {y=} ile eşit")
else:
    print(f"{x=} sayısı {y=} den küçük")