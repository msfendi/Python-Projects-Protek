def beliBuah(buah):

    print("Daftar Harga Buah")
    for a, i in buah.items():
        print("-", a, "( Harga Rp", i, ")")

    listHarga = []
    beliLain = True

    while(beliLain == True):
        a = input("masukkan nama buah = ")
        key = buah.keys()

        if(a not in key):
            print("buah tidak ditemukan")
            continue
        else:
            cek = True
            while(cek ==True):
                try:
                    jumlah = int(input("masukkan kg = "))
                    i = buah.get(a)
                    harga = i * jumlah
                    listHarga.append(harga)
                    cek = False

                except ValueError:
                    print("masukkan nilai dengan benar")
                    continue

            pilihan = input("Beli buah yang lain (y/n) ? ")
            if (pilihan == "y" or pilihan == "Y"):
                beliLain = True
            elif (pilihan == "n" or pilihan == "N"):
                beliLain = False
            else:
                print("Inputan tidak benar, Program akan keluar otomatis")
                break

    print("-" * 20)
    totalHarga = sum(listHarga)
    print("Total Harga : ", totalHarga)



def tambahBuah(buah):
    pengecekan = True
    while(pengecekan == True):
        namaBuah = input("Masukkan nama buah = ")
        daftarBuah = buah.keys()

        if(namaBuah not in daftarBuah):
            hargaSatuan = int(input("Masukkan harga satuan = "))
            buah[namaBuah] = hargaSatuan
            print("Data Buah :")
            for a, i in buah.items():
                print("-", a, "( Harga Rp", i, ")")
            pengecekan = False
        else:
            print("Buah tersebut telah terdaftar")
            continue


def hapusBuah(buah):

    pengecekan = True
    while (pengecekan == True):
        delBuah = input("Masukkan nama buah yang ingin dihapus = ")
        daftarBuah = buah.keys()

        if(delBuah in daftarBuah):
            del buah[delBuah]
            print("Buah", delBuah, "telah dihapus")
            print("Data Buah :")
            for a, i in buah.items():
                print("-", a, "( Harga Rp", i, ")")
            pengecekan = False
        else:
            print("Buah tidak ditemukan")
            continue


print("Menu")
print("A. Tambah data buah")
print("B. Beli buah")
print("C. Hapus buah")
print("keluar")

buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}

pengecekan = True
while(pengecekan == True):
    pilihan = input("Pilihan Menu (a/b/c/keluar) = ")
    if (pilihan == "A" or pilihan == "a"):
        tambahBuah(buah)
        # pengecekan = False
    elif (pilihan == "B" or pilihan == "b"):
        beliBuah(buah)
        pengecekan = False
    elif (pilihan == "C" or pilihan == "c"):
        hapusBuah(buah)
    elif (pilihan == "keluar"):
        break
    else:
        print("Inputan tidak benar")