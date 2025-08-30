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

from library import komut

# with open("notlar.txt", "r+") as dosya:
#   dosya.readlines()
#   dosya.write(metin + "\n")