"""
kullanicidan bir pixelin renk tanimlamasi olan rgb degerini alip
bu rengin karsi rengini yani negatifini veren bir fonksiyon
yazmak istiyoruz. Eğer kullanıcı 'cikis' yazarsa uygulama bitirilmeli.

negatif değeri bulmak için, renk değerini 255'den çıkartarak
bulabilirsiniz.
"""

def color_reverse(r, g, b):
    return (255-r, 255-g, 255-b)

while True:
    renk = input("Renk (R,G,B): ") # 11,66,87
    renkler = renk.split(",") # ["11", "66", "87"]
    red = int(renkler[0])
    green = int(renkler[1])
    blue = int(renkler[2])

    (r, g, b) = color_reverse(red, green, blue) # (244, 189, 168)
    
    print(f"{r},{g},{b}")