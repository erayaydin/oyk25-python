kelimeler = [
    "Python",
    "Programlama",
    "ÖzgürYazılım",
    "FOSS"
]
"""
Yukarıdaki kelimeleri bir sözlük içerisinde harf
sayısı ile gösteriniz. Örneğin;
{'Python': 6, 'Programlama': 11, 'ÖzgürYazılım': 12, 'FOSS': 4}
"""
sonuc = {}
for kelime in kelimeler:
    sonuc[kelime] = len(kelime)
print(sonuc)

sonuc = { kelime: len(kelime) for kelime in kelimeler }
print(sonuc)