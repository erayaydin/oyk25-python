"""
Bu modül öğrencilerle ilgili işlemleri kapsamaktadır.
"""
ogrenciler = {
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

def ogrencileri_kaydet():
	import csv
	with open("ogrenciler.csv", "w") as dosya:
		yazici = csv.writer(dosya)
		for ismi, bilgiler in ogrenciler.items():
			yazici.writerow([ismi, bilgiler["sinif"], bilgiler["kitap"]])

# ogrencileri_kaydet()

def ogrencileri_oku():
	global ogrenciler
	import csv
	with open("ogrenciler.csv", "r") as dosya:
		okuyucu = csv.reader(dosya)
		ogrenciler = {}
		for satir in okuyucu:
			ogrencinin_kitabi = None if satir[2] == '' else satir[2]
			ogrenciler[satir[0]] = { "isim": satir[0], "sinif": satir[1], "kitap": ogrencinin_kitabi }

# ogrencileri_oku()
# print(ogrenciler)

def ogrenci_ekle(isim, sinif):
	"""
	Öğrenciler sözlüğüne yeni bir öğrenci ekler.
	"""
	ogrenciler[isim] = { "isim": isim, "sinif": sinif, "kitap": None }
	ogrencileri_kaydet()

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
	ogrencileri_kaydet()

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
	silinen_ogrenci = ogrenciler.pop(isim, None)
	ogrencileri_kaydet()
	return silinen_ogrenci

"""
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
"""