takimlar = ["Galatasaray", "Fenerbahçe", "Beşiktaş"]
sayici = enumerate(takimlar, start=1)

kacinci_takim, takim_adi = next(sayici)
print(f"{kacinci_takim}. takım: {takim_adi}")
kacinci_takim, takim_adi = next(sayici)
print(f"{kacinci_takim}. takım: {takim_adi}")
kacinci_takim, takim_adi = next(sayici)
print(f"{kacinci_takim}. takım: {takim_adi}")
