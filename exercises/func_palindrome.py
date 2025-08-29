"""
Herhangi bir metnin tersten yazılmışı ile aynı olup olmadığını
kontrol etmek için bir fonksiyon yazınız. Dönüş değeri True veya False
olmalı.
"""
def palindrome_mu(metin):
	return metin == metin[::-1]

print(palindrome_mu("eray")) # False
print(palindrome_mu("aba")) # True
print(palindrome_mu("abacaba")) # True
print(palindrome_mu("abacdaba")) # False