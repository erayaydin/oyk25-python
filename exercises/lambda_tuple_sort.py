"""
Vize ve final puanları tuple içerisinde yer alan öğrencileri
en yüksekten en düşüğe sıralayınız.
"""

ogrenciler = [
    ("Eray", 70, 50),
    ("Mustafa", 90, 60),
    ("Ali", 10, 15),
    ("Ahmet", 88, 20),
]

print("Öğrenciler:")
print(ogrenciler)
basari_siralamasi = sorted(ogrenciler, key=lambda o: o[1] + o[2], reverse=True)
print("Başarılı öğrenci sıralaması:")
print(basari_siralamasi)