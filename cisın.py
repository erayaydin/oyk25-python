import json

ogrenciler = {
    'Eray': {
        'yas': 29,
    },
    'Mustafa': {
        'yas': 18,
    },
}

with open('file.json', 'w') as dosya:
    dosya.write(json.dumps(ogrenciler))

with open('file.json', 'r') as dosya:
    ogrenciler = json.loads(dosya.read())

print(ogrenciler)