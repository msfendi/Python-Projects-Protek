a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

a.insert(3, 10)
b.insert(2, 15)

a.append(4)
b.append(8)

a.sort()
print(a)
b.sort()
print(b)

c = a[0:8].copy()
print(c)
d = b[2:10].copy()
print(d)

e = []
for i,u in zip(c,d):
    jumlah = (i + u)
    e.append(jumlah)
print("e = ",e)

minE = min(e)
print("nilai min = ", minE)

maxE = max(e)
print("nilai max = ", maxE)

sumE = sum(e)
print("nilai sum = ", sumE)