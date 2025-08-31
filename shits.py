import csv

oyuncular = [
    ["Galadrin", 80, "Warrior", ("Potion", "Item1"), { "boss": False }],
    ["LLorva", 10, "Paladin", ("Potion", "Item1"), { "boss": False }],
    ["Laernia", 15, "Hunter", ("Potion", "Item1"), { "boss": False }],
]

with open('example.csv', 'r') as dosya:
    shiiit = csv.reader(dosya, delimiter=":")
    for satir in shiiit:
        print(f"[{satir[1]}] {satir[0]} {satir[2]} sınıfında")

with open('karakter.csv', 'w') as dosya:
    yazici = csv.writer(dosya, delimiter=":")
    yazici.writerows(oyuncular)