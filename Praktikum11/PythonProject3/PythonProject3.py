from datetime import *
myFile = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum11/datapeminjaman.txt', 'r')
read = myFile.readlines()
jumlahData = len(read)
data = False
listDictionary = []


def diffDate(x):
    k = x.split("-")
    tglskrg = datetime.date(datetime.now())
    tgllalu = date(int(k[0]), int(k[1]), int(k[2]))

    selisih = (tglskrg - tgllalu).days
    return selisih


cari = input('Masukkan Kode Member : ')

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
    tglskrg = datetime.date(datetime.now())
    print('')
    print('Data Peminjaman Buku')
    print(' Kode Member               : ', a[0], '\n',
          'Nama Member               : ', a[1], '\n',
          'Judul Buku                : ', a[2], '\n',
          'Tanggal Mulai Peminjaman  : ', a[3], '\n',
          'Tanggal Maks Peminjaman   : ', a[4],
          'Tanggal Pengembalian      : ', tglskrg)

    terlambat = diffDate(a[4])
    denda = terlambat * 2000

    if(terlambat < 0):
        print(' Terlambat                 :  0 hari', '\n',
          'Denda                     :  Rp 0')
    else:
        print(' Terlambat                 : ', terlambat, 'hari', '\n',
              'Denda                     : ', 'Rp', denda)

elif(data == False):
    print('Data Member tidak ditemukan')