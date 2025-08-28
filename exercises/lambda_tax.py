"""
`func_tax.py`'deki fonksiyonunuzu kullanarak listedeki her
fiyata aşağıdaki vergileri ekleyin ve yeni listeyi tek satırda
elde edin.
"""

fiyatlar = [100, 167.30, 5, 100]


def kdv_ekle(tutar, oran=0.18):
    return tutar * (1 + oran)


# oran=0.18 olmalı
kdv_18 = list(map(kdv_ekle, fiyatlar))
# oran=0.2 olmalı
kdv_20 = list(map(lambda f: kdv_ekle(f, 0.2), fiyatlar))