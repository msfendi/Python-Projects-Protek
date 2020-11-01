# Function Faktorial
def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil = hasil * i
    return hasil

print('Contoh Faktorial 5 adalah = ',faktorial(5))
print('')

# Function Kombinasi
def combinasi(n, m):
    selisih = n - m
    combinasi = faktorial(n)/(faktorial(selisih) * faktorial(m))
    return combinasi

# Contoh Soal Kombinasi
print('a. C(5, 3) = ', end='')
print(combinasi(5, 3))

print('')

# Function Permutasi
def permutasi(n, r):
    selisih = n - r
    permutasi = faktorial(n) / faktorial(selisih)
    return permutasi

# Contoh Soal Permutasi
print('b. P(10, 7) = ', end='')
print(permutasi(10, 7))