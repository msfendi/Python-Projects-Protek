myFile = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject5/text5.txt', 'r')
read = myFile.readlines()
jumlahData = len(read)
listsementara = []


for i in range(jumlahData):
    a = read[i].split('|')
    e = int(a[0]) + int(a[1])
    listsementara.append(e)

myFile.close()
hasil = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject5/hasil.txt', 'w')

for i in listsementara:
    hasil.write(str(i) + '\n')
hasil.close()

print('Cek file hasil')