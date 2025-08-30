"""
Bu modül kitaplarla ilgil işlemleri kapsamaktadır.
"""
kitaplar = {}

def kitap_ekle(isim, sayfa=None, ogrenci=None):
	"""
	Kitaplar sözlüğüne yeni bir kitap ekler.
	"""
	deger = { "sayfa": sayfa, "ogrenci": ogrenci }
	kitaplar[isim] = deger
	#kitaplar.update({ isim: deger })

# kitap_ekle("Kitap 1", 100)
# kitap_ekle("Kitap 2")
# kitap_ekle("Kitap 3", ogrenci="Mustafa")
# print(kitaplar)

"""
{
	'Kitap 1': {
		'sayfa': 100,
		'ogrenci': None
	},
	'Kitap 2': {
		'sayfa': None,
		'ogrenci': None
	},
	'Kitap 3': {
		'sayfa': None,
		'ogrenci': 'Mustafa'
	}
}
"""

def kitap_ara(isim):
	"""
	Kitaplar sözlüğünde bir ismi arar ve eğer bulursa o sözlük
	elemanını döndürür.
	"""
	return kitaplar[isim] if isim in kitaplar else None
	# if isim in kitaplar:
	#	return kitaplar[isim]
	#else:
	#	return None

def kitap_emanet(isim, ogrenci):
	"""
	Kitaplar sözlüğündeki elemanın 'ogrenci' anahtarını belirtilen
	öğrenci ile günceller
	"""
	kitap = kitap_ara(isim)
	# kitap["ogrenci"] = ogrenci
	# kitaplar.update({ isim: kitap })	
	if kitap:
		kitap["ogrenci"] = ogrenci

# kitap_emanet("Anna Karenina", "Mustafa")
# kitap_emanet("Anna Karenina", None)
def kitap_sil(isim):
	"""
	Kitaplar sözlüğündeki ilgili kitabı siler.
	"""
	# del kitaplar[isim]
	return kitaplar.pop(isim, None)
