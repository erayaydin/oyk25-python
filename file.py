"""
dosya = open("/Users/eray/test.txt")
try:
    ...
finally:
    dosya.close()

with open("/Users/eray/test.txt") as dosya:
    print(dosya.readlines())
"""
from datetime import datetime

with open("gunluk.txt", "r+") as dosya:
    gunlukler = dosya.readlines()
    for gunluk in gunlukler:
        parcalar = gunluk.split("|", 1)
        tarih = parcalar[0]
        metin = parcalar[1].strip()
        print(f"Tarih: {tarih}")
        print(f"Günlük: {metin}")
        print("========")

gunluk = input("Günlük Metni: ") # "Deneme"
bugun = datetime.now() # 2025-08-30 16:11:00
with open("gunluk.txt", "a") as dosya:
    tarih = bugun.strftime("%Y-%m-%d %H:%M:%S")
    dosya.write(f"{tarih}|{gunluk}\n")

