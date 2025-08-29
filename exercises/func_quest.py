"""
Herhangi bir görevi `odul`, `dakika` ve `zorluk` değerlerine göre
puanlayacak olan `gorevi_puanla` fonksiyonunu yazınız. Ardından
`en_iyi_gorev` fonksiyonu ile aşağıda yer alan görevlerden en
iyi olanını ekrana yazdırınız.

Formül: (odul/dakika)*(4-zorluk)
"""

gorevler = [
    {"ad": "G1", "odul": 90, "dakika": 120, "zorluk": 1},
    {"ad": "G2", "odul": 60, "dakika": 80, "zorluk": 2},
    {"ad": "G3", "odul": 30, "dakika": 60, "zorluk": 2},
]

def puan_hesapla(odul, dakika, zorluk=1):
    return (odul/dakika)*(4-zorluk)

def en_iyi_gorev(*gorevler):
    max(gorevler, key=lambda g: puan_hesapla(g["odul"], g["dakika"], g["zorluk"]))
    en_yuksek_puanli_gorev = None
    en_yuksek_puan = 0
    for gorev in gorevler:
        gorev_puani = puan_hesapla(gorev["odul"], gorev["dakika"], gorev["zorluk"])
        if gorev_puani > en_yuksek_puan:
            en_yuksek_puan = gorev_puani
            en_yuksek_puanli_gorev = gorev
    return en_yuksek_puanli_gorev

print(en_iyi_gorev(*gorevler))
print(en_iyi_gorev(gorevler[0], gorevler[1], gorevler[2]))