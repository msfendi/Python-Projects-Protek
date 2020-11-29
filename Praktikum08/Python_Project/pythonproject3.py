n = 0
a = []
m = int(input("Berapa banyak = "))
while (n < m):
    nama = input("masukkan nama =")
    a.append(nama)
    n += 1
print("=========== HASIL ============")
a.sort()
for i in a:
    print(i, "(" , len(i), 'karakter)')