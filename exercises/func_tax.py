"""
Bir KDV hesaplama fonksiyonu yazınız.
"""

def kdv_ekle(tutar, oran=0.18):
	kdvli_hali = tutar * (1 + oran)
	return kdvli_hali

deger1 = kdv_ekle(100)
deger2 = kdv_ekle(130, oran=0.2)
deger2 = kdv_ekle(130, oran=0.3)
deger2 = kdv_ekle(130, oran=0.4)
deger2 = kdv_ekle(190, oran=0.2)
deger2 = kdv_ekle(200, oran=0.1)

print(f"{deger1=}") # print(f"deger1={deger1}") # 118
print(f"{deger2=}") # print(f"deger2={deger2}") # 156