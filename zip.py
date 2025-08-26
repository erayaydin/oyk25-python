"""
ogrenciler = ["Eray", "Mustafa", "Ali", "Ahmet", "Ayşe"]
puanlar = [90, 100, 80, 70]

print(list(zip(ogrenciler, puanlar)))
"""

ulkeler = ["Türkiye", "Japonya", "Fransa"]
baskentler = ["Ankara", "Tokyo", "Paris"]
nufus = [1000, 2000, 3000]

ulkeler_ve_baskentleri = zip(ulkeler, baskentler, nufus) # [(), (), ()...]
for ulke, baskent, nufus in ulkeler_ve_baskentleri:
    print(f"{ulke} ülkesinin başkenti: {baskent} ve nüfusu: {nufus}")
