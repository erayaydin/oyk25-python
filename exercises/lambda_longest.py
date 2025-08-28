"""
Girilen bir cümle içerisindeki en uzun kelimeyi
ekrana yazan bir betik geliştiriniz.
"""

cumle = input("Cümle: ")
en_uzun_kelime = max(cumle.split(), key=lambda k: len(k))
print(f"En uzun kelime: {en_uzun_kelime}")