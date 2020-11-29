a = []
b = 0
n = int(input("berapa banyak ? "))
while b < n:
    angka = int(input("masukkan angka ? "))
    a.append(angka)
    b += 1
a.sort(reverse=True)
print(a)