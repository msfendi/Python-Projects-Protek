u = True
myFile = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject2/text2.txt', 'a')
while (u == True):
    nim = input("Masukkan NIM : ")
    nama = input("Masukkan Nama Mhs : ")
    alamat = input("Masukkan Alamat : ")
    myFile.write(nim + "|" + nama + "|" + alamat + "\n")

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