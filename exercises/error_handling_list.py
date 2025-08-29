secimler = ["ekle", "cikart", "bol", "carp"]
while True:
    for i,secim in enumerate(secimler):
        print(f"{i+1}) {secim}")
    secim = input("> ")
    try:
        yapilan_secim = secimler[int(secim)-1]
        print(f"Kullanıcının seçtiği: {yapilan_secim}")
    except IndexError:
        print("Yanlış seçim yaptın.")
    except ValueError:
        print("Sadece sayı giriniz.")