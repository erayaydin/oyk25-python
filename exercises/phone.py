"""
Telefon formatlayıcı: 10 haneli numarayı "(xxx) xxx xx xx" biçiminde
yaz. '0' ile başlayan 11 hane girilirse baştaki sıfırı at.
> Telefon: 05301234567
tel = "5301234567"
(530) 123 45 67
"""
tel = input("Telefon: ")

rakamlar = "".join(ch for ch in tel if ch.isdigit())
if len(rakamlar) == 11 and rakamlar.startswith("0"):
    rakamlar = rakamlar[1:]
if len(rakamlar) != 10:
    print("Geçersiz numara.")
else:
    print(f"({rakamlar[0:3]}) {rakamlar[3:6]} {rakamlar[6:8]} {rakamlar[8:10]}")