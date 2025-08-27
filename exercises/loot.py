"""
Kullanıcıdan bir koordinat alın ve aşağıdaki listeye göre karşılık
gelen durumu ekrana yazdırın. Kullanıcı 'cikis' yazarsa bitirin.
- "kılıç": Bir kılıç kazandın!
- "düşman": Bir düşmanla karşılaştın.
- "altın": Bir altın kazandın

> Koordinat: 1x4
Bir kılıç kazandın!
> Koordinat: 3x2
Burada bir şey yok...
> Koordinat: cikis
Güle güle!
"""
entities = { "kılıç": (1,4), "düşman": (3,1), "altın": (2,2) }

while True:
    girilen = input("Koordinat: ") # "1x4"
    if girilen == "cikis":
        break
    koordinatlar = girilen.split("x") # ["1", "4"]
    if len(koordinatlar) != 2:
        print("Düzgün koordinat gir! Format: 1x1")
        continue
    if koordinatlar[0].isdigit() or not koordinatlar[1].isdigit():
        print("Koordinatlar sayı olmalıdır!")
        continue
    x = int(koordinatlar[0]) # 1
    y = int(koordinatlar[1]) # 4
    bulunan_esya = None
    for isim, (esya_x, esya_y) in entities.items(): # [ ("kılıç", (1,4)), ("düşman", (3,1)), ("altın", (2,2)) ]
        if esya_x == x and esya_y == y:
            bulunan_esya = isim
    if bulunan_esya == "kılıç":
        print("Bir kılıç kazandın!")
    elif bulunan_esya == "düşman":
        print("Bir düşmanla karşılaştın.")
    elif bulunan_esya == "altın":
        print("Bir altın kazandın")
    else:
        print("Burada bir şey yok...")