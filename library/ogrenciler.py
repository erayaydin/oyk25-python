"""
Bu modül öğrencilerle ilgili işlemleri kapsamaktadır.
"""
ogrenciler = {}

"""
{
	"Eray": {
		"isim": "Eray",
		"sinif": "Python ile Programlamaya Giriş",
		"kitap": None
	},
	"Mustafa": {
		"isim": "Mustafa",
		"sinif": "Python ile Programlamaya Giriş",
		"kitap": "Anna Karenina"
	}
}
"""

def ogrenci_ekle(isim, sinif):
	"""
	Öğrenciler sözlüğüne yeni bir öğrenci ekler.
	"""
	ogrenciler[isim] = { "isim": isim, "sinif": sinif, "kitap": None }

def ogrenci_ara(isim):
	"""
	Öğrenciler sözlüğünde bir ismi arar ve eğer bulursa o sözlük
	elemanını döndürür.
	"""
	return ogrenciler[isim] if isim in ogrenciler else None
	# if isim in ogrenciler:
	#	return ogrenciler[isim]
	#else
	# 	return None

def ogrenci_kitap_ekle(isim, kitap):
	"""
	Öğrenciler sözlüğündeki öğrenciyi bulup 'kitap' anahtarını ödünç
	aldığı kitap ile değiştirir.
	"""
	ogrenci = ogrenci_ara(isim)
	if ogrenci:
		ogrenci["kitap"] = kitap

def ogrenci_kitap_sil(isim):
	"""
	Öğrenciler sözlüğündeki öğrenciyi bulup 'kitap' anahtarını None olarak
	değiştirir.
	"""
	ogrenci_kitap_ekle(isim, None)


def ogrenci_sil(isim):
	"""
	Öğrenciler sözlüğündeki öğrenciyi sözlükten siler.
	"""
	return ogrenciler.pop(isim, None)

if __name__ == "__main__":
	ogrenci_ekle("Eray", "Python ile Programlamaya Giriş")

	print(ogrenci_ara("Eray"))
	print(ogrenci_ara("Mustafa"))

	ogrenci_ekle("Mustafa", "Python ile Programlamaya Giriş")
	print("Yeni öğrenci eklendi!", ogrenciler)
	ogrenci_kitap_ekle("Mustafa", "Anna Karenina")
	print("Mustafa kitap aldı", ogrenciler)
	ogrenci_kitap_sil("Mustafa")
	print("Mustafa kitabı geri verdi", ogrenciler)

	print(ogrenciler)
	ogrenci_sil("Eray")
	print(ogrenciler)