myFile = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject3/text3.txt', 'r')
read = myFile.readlines()
jumlahData = len(read)
data = False
listDictionary = []
cari = input('Masukkan NIM yang mau dicari : ')
for i in range(jumlahData):
    a = read[i].split('|')
    listDictionary.append(a)
    if cari == a[0]:
        data = True
        break
    else:
        data = False

if (data == True):
    a = read[i].split('|')
    print('Data Mahasiswa')
    print(' NIM : ', a[0], '\n', 'Nama : ', a[1], '\n', 'Alamat : ', a[2])
elif(data == False):
    print('Data Mahasiswa tidak ditemukan')