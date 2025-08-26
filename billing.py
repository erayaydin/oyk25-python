"""
Bir mobil hat kullanıcısının o ay ne kadar ödemesi gerektiğini
hesaplayan bir betik hazırlamak istiyoruz. Kullanıcı tarifesine
ait ücreti, dakika hakkını ve internet (gb) hakkını girmeli. Ardından
o ay ne kadar dakika ve internet (gb) kullandığını girerek aşağıdaki
indirim ve tarife aşım ücretleriyle o ay ödemesi gereken tutarı
öğrenebilmeli.

- Dakika aşım ücreti (dk): 1
- İnternet aşım ücreti (GB): 100
- Toplam tutar 300'den fazla ise %10 indirim
- toplam tutar 500'den fazla ise %30 indirim
"""
tarife_ucreti = int(input("Tarife ücretini giriniz: "))
dakika_hakki = int(input("Tarifenize dahil dakika hakkınızı giriniz: "))
internet_hakki = int(input("Tarifenize dahil internet hakkınızı giriniz: "))
dakika_kullanim = int(input("Bu ay kaç dk kullandınız? "))
internet_kullanim = int(input("Bu ay kaç gb internet kullandınız? "))

toplam = tarife_ucreti

if dakika_kullanim > dakika_hakki:
    dakika_asim = dakika_kullanim - dakika_hakki
    toplam += dakika_asim

if internet_kullanim > internet_hakki:
    internet_asim = internet_kullanim - internet_hakki
    toplam += internet_asim * 100

if toplam > 500:
    toplam *= 0.7
elif toplam > 300:
    toplam *= 0.9

print(f"Ödeyeceğiniz toplam tutar: {toplam}")