emails = [
    "eray.aydin@fingerprint.com",
    "mustafa.yagci@hubx.com",
    "delifisek07@crazyboy.com",
    "ozguryazilim@gmail.com",
    "eray@gmail.com",
    "mustafa@gmail.com",
    "ozguryazilim@disroot.org",
]
"""
E-postaların her birinin uzantısını bir küme içerisinde
birleştirin.
{ "fingerprint.com", "hubx.com", "crazyboy.com", ... }
"""

domainler = set()
for email in emails:
    kisimlar = email.split("@") # ['....', 'gmail.com]
    domainler.add(kisimlar[1])
print(domainler)

domainler = { email.split("@")[1] for email in emails }
print(domainler)
