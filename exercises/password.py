"""
Kullanıcının girdiği parolanın güçlü olup olmadığını test edeceğiz.
Girilen parolanın en az 8 karakter olması, 1 büyük harf ve 1 sayıya
sahip olması gerekiyor. Güçlü parola girene kadar program çalışmaya
devam etmeli.
> Parola: abcd
Çok zayıf bir parola girdiniz lütfen tekrar girin.
> Parola: abcdefgH
Çok zayıf bir parola girdiniz lütfen tekrar girin.
> Parola: abcdefg1
Çok zayıf bir parola girdiniz lütfen tekrar girin.
> Parola: abcdeFg1
Güçlü!
Yeni parolanız sisteme kaydedildi, görüşürüz!
"""
while True:
    parola = input("Parola: ")
    if len(parola) >= 8:
        sayi_var_mi = False
        buyuk_harf_var_mi = False
        for karakter in parola:
            if karakter.isdigit():
                sayi_var_mi = True
            if karakter.isupper():
                buyuk_harf_var_mi = True
        if sayi_var_mi and buyuk_harf_var_mi:
            print("Güçlü!")
            break
        else:
            print("Çok zayıf bir parola girdiniz lütfen tekrar girin.")
    else:
        print("Çok zayıf bir parola girdiniz lütfen tekrar girin.")
print("Yeni parolanız sisteme kaydedildi, görüşürüz!")