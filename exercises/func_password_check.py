"""
Bir parola güç kontrol fonksiyonu yazınız. Bu fonksiyon parametre
olarak minimum karakter sayısı, kaç tane sayı olmalı, kaç tane
büyük harf olmalı değerlerine göre boolean (True/False) değer
döndürmeli.
"""
def parola_kontrol(parola, min_uzunluk=8, sayi=1, buyuk_harf=1):
	# sum(karakter.isdigit() for karakter in parola)
	return len(parola) >= min_uzunluk and \
		len([karakter for karakter in parola if karakter.isdigit()]) >= sayi and \
		sum([1 for karakter in parola if karakter.isupper()]) >= buyuk_harf and
	"""
	if len(parola) < min_uzunluk:
		return False
	
	buyuk_harf_adeti = 0
	sayi_adeti = 0
	for karakter in parola:
		if karakter.isdigit():
			sayi_adeti += 1
		elif karakter.isupper():
			buyuk_harf_adeti += 1
	
	if sayi_adeti < sayi:
		return False
	
	if buyuk_harf_adeti < buyuk_harf:
		return False
	
	return True
	"""

print(parola_kontrol("eray")) # False
print(parola_kontrol("Eray1")) # False
print(parola_kontrol("Guclu1Parola55", buyuk_harf=3, sayi=3)) # False
print(parola_kontrol("Guclu1Parola55", buyuk_harf=3, sayi=4)) # False
print(parola_kontrol("Guclu1Parola", buyuk_harf=2)) # True
print(parola_kontrol("CokGucluParola123", sayi=4, buyuk_harf=4)) # False