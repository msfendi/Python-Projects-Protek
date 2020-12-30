myfile = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject1/text1.txt', 'r')
teks = myfile.readlines()
a = list(teks)
c = []
for i in a:
    b = int(i)
    d = c.append(b)

ganjil = 0
genap = 0
for u in c:
    if (u % 2 == 0):
        genap += 1
    else:
        ganjil += 1

print("Banyaknya bilangan genap : ",genap)
print("Banyaknya bilangan genap : ",ganjil)