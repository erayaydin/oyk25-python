sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

# print(sayi1, sayi2) --> 10 7
print("Toplama yapmak için +, Çıkartma yapmak için -, Çarpma yapmak için *, Bölme yapmak için / girebilirsiniz.")
islem = input("İşlem: ")
# print(f"İşleminiz: {islem}")

if islem == "+":
    toplam = sayi1 + sayi2
    print(f"Toplam: {toplam}")
elif islem == "-":
    cikartma = sayi1 - sayi2
    print(f"Çıkartma: {cikartma}")
elif islem == "*":
    carpim = sayi1 * sayi2
    print(f"Çarpım: {carpim}")
elif islem == "/" and sayi2 != 0:
    bolum = sayi1 / sayi2
    print(f"Bölüm: {bolum}")
else:
    print("Geçersiz bir işlem girdiniz")
print("Programı kullandınız!")

