"""
`card.py`'de yaptığınız kart bilgileri maskeleme
işlemini aşağıdaki liste elemanlarının hepsi
için tek satırda yapınız.
"""

cards = ["1234567812345678", "1749302756292743", "1663032757209287", "1648201647392846"]

masked = list(map(lambda k: "*" * (len(k) - 4) + k[-4:], cards))

print(masked)