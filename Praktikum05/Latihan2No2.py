# Perulangan Bilangan Ganjil dan Banyaknya Perulangan dengan For
hitung = 0
for ganjil in range(0, 100):
    if ganjil % 2 == 1:
        print(ganjil)
        hitung = hitung + 1

print('Banyaknya bilangan ganjil :', str(hitung))

# Perulangan Bilangan Ganjil dan Banyaknya Perulangan dengan While
hitung = 0
nilai = 0
while nilai <= 100:
    if nilai % 2 == 1:
        print(nilai)
        hitung = hitung + 1
    nilai = nilai + 1
print('Banyaknya bilangan ganjil :', str(hitung))