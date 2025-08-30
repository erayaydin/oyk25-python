"""
Komut satırı yardımcılarını barındırır.
"""
def baslik(metin, karakter="#"):
	"""
	Komut satırı arayüzüne başlık yazdırır. Örneğin;
	##########
	# Başlık #
	##########
	"""
	print(karakter * (len(metin) + 4))
	print(f"{karakter} {metin} {karakter}")
	print(karakter * (len(metin) + 4))

def listele_secim_al(liste):
	"""
	Gelen sözlüğe göre seçimleri listeler ve kullanıcının
	seçimini fonksiyonun kullanıldığı yere döndürür. Örneğin
	{ "ekle": "Kişi Ekle", "sil": "Kişi Sil" }
	için ekrana:
	1) Kişi Ekle
	2) Kişi Sil
	> 
	yazar ve kullanıcıdan input bekler. Gelen input'a göre return
	olarak "ekle" döndürür. Farklı bir input gelirse tekrar soru sorar.
	"""
	anahtarlar = list(liste.keys())

	for i, key in enumerate(anahtarlar, start=1):
		print(f"{i}) {liste[key]}")
	
	while True:
		secim = input("> ")
		if not secim.isdigit():
			print("Lütfen sayısal seçim yapınız.")
			continue
		secim = int(secim) # 1
		if secim < 1 or secim > len(anahtarlar):
			print(f"Lütfen 1 ve {len(anahtarlar)} arasında seçim yapın")
			continue
		break
	# 1) Ekle, 2) Sil, 3) Cikis
	# secim = 1 (ekle)
	# anahtarlar = ["ekle", "sil", "cikis"]
	return anahtarlar[secim-1]


kullanici_secim = listele_secim_al({
	"ekle": "Kullanıcı Ekle",
	"sil": "Kullanıcı Sil",
	"cikis": "Çıkış" }
)
print("Kullanıcı bunu seçti", kullanici_secim)