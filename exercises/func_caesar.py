"""
Sadece İngilizce alfabeyi destekleyen bir sezar şifreleme ve çözme
fonksiyonu yazacağız. Sezar şifrelemesinde her *harf* alfabede
belirtilen bir miktar kadar sağa kaydırılır. Alfabenin dışına çıkan
harflerde başa dönmesi için (% yani mod, İngilizce için 26)
kullanılabilir. Fonksiyonlar aşağıdaki formatta olmalı.

Not: `ord` ile bir karakterin unicode değerini, `chr` ile de unicode
değerini karaktere dönüştürebilirsiniz.
"""
def sifrele(metin, miktar=3):
    kaydirilmis = []
    for karakter in metin:
        bu_karakter_kaydirildi = kaydir(karakter, miktar)
        kaydirilmis.append(bu_karakter_kaydirildi)
    return "".join(kaydirilmis)
    

def coz(metin, miktar=3):
    return sifrele(metin, -miktar)

def kaydir(karakter, miktar):
    if 'a' <= karakter <= 'z': # karakter = 121
        baslangic = ord('a') # 97
        karakterin_kodu = baslangic + (ord(karakter) - baslangic + miktar) % 26
        return chr(karakterin_kodu)
    if 'A' <= karakter <= 'Z':
        baslangic = ord('A')
        karakterin_kodu = baslangic + (ord(karakter) - baslangic + miktar) % 26
        return chr(karakterin_kodu)
    return karakter

print(sifrele("Bu cok gizli bir mesaj", miktar=3))