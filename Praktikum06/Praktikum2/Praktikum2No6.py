def luasSegitiga(a, t):
    luas = a * t / 2
    return luas

# SEGITIGA PERTAMA
alas = 10
tinggi = 20
print('Luas segitiga pertama dengan alas', alas,
      'dan tinggi', tinggi,
      'adalah', luasSegitiga(alas, tinggi))

print('-'*60)

# SEGITIGA KEDUA
alas2 = 15
tinggi2 = 45
print('Luas segitiga kedua dengan alas', alas2,
      'dan tinggi', tinggi2,
      'adalah', luasSegitiga(alas2, tinggi2))