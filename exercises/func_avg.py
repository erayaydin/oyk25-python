"""
Parametre olarak girilen tüm sayıların ortalamasını bulan
fonksiyonu yazınız. Dönüş değeri float olmalı.
"""
def ortalama(*sayilar):
	print(f"Bana gelen sayılar: {sayilar}")
	# return sum(sayilar) / adet if (adet:=len(sayilar)) > 0 else 0.0
	toplam = sum(sayilar)
	for sayi in sayilar:
		toplam += sayi
	sayi_adeti = len(sayilar)
	if sayi_adeti == 0:
		return 0.0
	ortalama_degeri = toplam / sayi_adeti
	return ortalama_degeri

deger1 = ortalama(1,2,3)
print(f"{deger1=}")
deger2 = ortalama(1,2,3,4,5,6)
print(f"{deger2=}")
deger3 = ortalama(1)
print(f"{deger3=}")
deger4 = ortalama()
print(f"{deger4=}")