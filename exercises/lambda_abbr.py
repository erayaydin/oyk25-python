"""
Girilen bir metnin baş harflerini birleştiren
yani kısaltmasını veren halini yazınız.
"""

uzun_hali = input("Terim: ")
kisa_hali = "".join(map(lambda k: k[0].upper(), uzun_hali.split(" ")))
print(f"Kısa hali: {kisa_hali}")