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

def en_iyi_gorev(*gorevler):
    pass

print(en_iyi_gorev(*gorevler))