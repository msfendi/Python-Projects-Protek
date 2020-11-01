# Perulangan Bilangan Ganjil, Menghitung Banyaknya Perulangan, dan Menghitung Jumlah Bilangan dengan For
hitung = 0
sum = 0
for ganjil in range(0, 100):
    if ganjil % 2 == 1:
        print(ganjil)
        sum = sum + ganjil
        hitung = hitung + 1

print('Banyaknya bilangan ganjil :', str(hitung))
print('Jumlah seluruh bilangan :', str(sum))

# Perulangan Bilangan Ganjil, Menghitung Banyaknya Perulangan, dan Menghitung Jumlah Bilangan dengan For
hitung = 0
sum = 0
nilai = 0
while nilai <= 100:
    if nilai % 2 == 1:
        print(nilai)
        sum = sum + nilai
        hitung = hitung + 1
    nilai = nilai + 1
print('Banyaknya bilangan ganjil :', str(hitung))
print('Jumlah seluruh bilangan :', str(sum))