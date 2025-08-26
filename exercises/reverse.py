"""
Girilen bir cümleyi tersine çevirin.
> Cümle: Python ile programlamaya giriş
şirig ayamalmargorp eli nohtyP

Her bir kelimeyi ayrı tersine çevirin.
> Cümle: Python ile programlamaya giriş
nohtyP eli ayamalmargorp şirig
"""
cumle = input("Cümle: ") # Python ile programlamaya giriş

"""
ters_kelimeler = [kelime[::-1] for kelime in cumle.split()]
"""

"""
ters_kelimeler = []
for kelime in kelimeler:
    ters_kelimeler.append(kelime[::-1])
"""

ters_hali = " ".join([kelime[::-1] for kelime in cumle.split()])
print(ters_hali)

"""
ters_hali = ""
for ters_kelime in ters_kelimeler:
    ters_hali += ters_kelime + " "
print(ters_hali)
"""

#print(cumle[::-1])

"""
ters = ""
for i in range(len(cumle)-1, -1, -1):
    print(cumle[i], end="")
    ters += cumle[i]
print(ters)
"""

"""
harfler = []
for karakter in cumle:
    harfler.append(karakter)
harfler.reverse()
print(harfler)

ters = ""
for harf in harfler:
    ters += harf
print(ters)

ters = "".join(harfler)
print(ters)
"""

