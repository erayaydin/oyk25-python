"""
Daha önceki yaptığımız komut modülünü de kullanarak
kullanıcının "kalıcı" not ekleyip listeleyebileceği
bir uygulama yazınız.
############
# Ana Menü #
############
1) Notları Listele
2) Yeni Not Ekle
3) Notları Temizle
4) Çıkış
> 1

##########
# Notlar #
##########
1) 2025-08-30 16:39:00
2) 2025-08-30 16:38:00
3) 2025-08-30 16:37:00
4) Ana Menü
> 1

#######################
# 2025-08-30 16:39:00 #
#######################
with, arkaplanda context manager ile
kullanılıyormuş. Yani ileride ben de
with ile çalışabilir veriler üretebilirim

Çıkmak için enter: 

#################
# Yeni Not Ekle #
#################
> ....
Not eklendi!
"""

from datetime import datetime
from library import komut

# with open("notlar.txt", "r+") as dosya:
#   dosya.readlines()
#   dosya.write(metin + "\n")

def cikis():
    import sys
    print("Çüüz")
    sys.exit(0)

def notlari_listele():
    notlarim = {}
    with open("notlar.json", "r") as dosya:
        import json
        """
        [
            {
                'tarih': '2025-08-30 18:32:28',
                'not': 'asdasdasda'
            },
            {
                'tarih': '2025-08-30 18:32:31',
                'not': 'cascascsacasca'
            }
        ]
        """
        jsondaki_notlar = json.loads(dosya.read())
        for notum in jsondaki_notlar:
            notlarim[notum['tarih']] = notum['not']
        """
        for satir in dosya.readlines():
            # satir = "2025-08-29 18:19:00 | not uygulamamı | karakteri ile yaptım\n"
            parcala = satir.split(" | ", 1)
            tarih = parcala[0]
            notum = parcala[1].rstrip()
            #not = "dsfghj" # reserved keywords
            notlarim[tarih] = notum
        """
    #{
    #   "2025-08-09 01:00:00": "not 1",
    #   "2025-08-09 00:30:00": "not 2",
    #}
    komut.baslik("Notlarım")
    notlarim["anamenu"] = "Ana Menü"
    secimler = {tarih: tarih for tarih in notlarim}
    secim = komut.listele_secim_al(secimler)
    if secim == "anamenu":
        return
    komut.baslik(secim)
    print(notlarim[secim])
    input("Çıkmak için enter")
    

def not_ekle():
    import json
    notum = input("Not Giriniz: ")
    with open("notlar.json", "r+") as dosya:
        varolan_notlarim = json.loads(dosya.read())
    with open("notlar.json", "w") as dosya:
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        varolan_notlarim.append({
            "tarih": tarih,
            "not": notum,
        })
        dosya.write(json.dumps(varolan_notlarim, indent=4, sort_keys=True))
    print("Not kaydedildi.")
    input("Devam etmek için enter")

def not_temizle():
    dosya = open("notlar.txt", "w")
    dosya.close()

menu = {
    "listele": "Notları Listele",
    "ekle": "Yeni Not Ekle",
    "temizle": "Notları Temizle",
    "cikis": "Çıkış"
}

islemler = {
    "listele": notlari_listele,
    "ekle": not_ekle,
    "temizle": not_temizle,
    "cikis": cikis
}

while True:
    komut.baslik("Ana Menü")
    secim = komut.listele_secim_al(menu)
    islemler[secim]()
