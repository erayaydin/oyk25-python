"""
Kullanıcıdan bir başlık alınız. Ardından bunu çerçeve
içerisinde gösteriniz.

> Başlık: Selam
#########
# Selam #
#########

> Başlık: Uzun bir cümle burada yer alıyor
####################################
# Uzun bir cümle burada yer alıyor #
####################################
"""
baslik = input("Başlık: ")
print("#" * (len(baslik)+4))
print(f"# {baslik} #")
print("#" * (len(baslik)+4))