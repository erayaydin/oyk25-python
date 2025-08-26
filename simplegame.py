import random

"""
Program rastgele olarak taş/kağıt/makas seçsin.
Kullanıcının 'taş', 'kağıt', 'makas' seçimine göre

Bilgisayar: Taş
Sen: Kağıt
Kazandın!

veya

Bilgisayar: Makas
Sen: Kağıt
Kaybettin!

gibi bir çıktı versin ve betik bitsin.
"""

secenekler = ["taş", "kağıt", "makas"]
kullanici = input("taş / kağıt / makas : ")
bilgisayar = random.choice(secenekler)

print(f"Sen: {kullanici}")
print(f"Bilgisayar: {bilgisayar}")
if bilgisayar == kullanici:
    print("Berabere kaldın!")
elif (kullanici == "taş" and bilgisayar == "makas") or (kullanici == "kağıt" and bilgisayar == "makas") or (kullanici == "makas" and bilgisayar == "kağıt"):
    print("Sen Kazandın!")
else:
    print("Sen kaybettin!")