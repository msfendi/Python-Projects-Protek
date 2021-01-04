from datetime import *
u = True
myFile = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum11/datapeminjaman.txt', 'a')
while (u == True):
    kode = input("Masukkan Kode Member : ")
    nama = input("Masukkan Nama Member : ")
    judulbuku = input("Masukkan Judul Buku : ")
    tglpinjam = datetime.date(datetime.now())
    tglkembali = tglpinjam + timedelta(days=7)
    myFile.write(kode + "|" + nama + "|" + judulbuku + "|" + str(tglpinjam) + "|" + str(tglkembali) + "\n")

    a = False
    while (a == False):
        ulang = input("Ulangi input lagi (y/n) : ")
        if (ulang.lower() == 'y'):
            a = True
        elif (ulang.lower() == 'n'):
            a = True
            u = False
        else:
            print("Inputan tidak sesuai")
            a = False

myFile.close()