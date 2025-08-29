while True:
    try:
        sayi1 = input("Sayı 1: ")
        if sayi1 == "5":
            raise TypeError("5'i sayı olarak kabul etmiyorum")
        sayi2 = input("Sayı 2: ")
        ortalama = (float(sayi1) + float(sayi2)) / 2
        print(f"Ortalama: {ortalama}")
    except ValueError as e:
        print(f"Hata: {e.args[0]}")