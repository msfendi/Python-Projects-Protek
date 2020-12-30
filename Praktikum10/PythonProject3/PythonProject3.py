myFile = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject3/text3.txt', 'r')
read = myFile.readlines()
jumlahData = len(read)
listDictionary = []
for i in range(jumlahData):
    a = read[i].split('|')

    dataMhs = {'nim': a[0], 'nama': a[1], 'alamat': a[2].replace('\n','')}
    listDictionary.append(dataMhs)
print(listDictionary)