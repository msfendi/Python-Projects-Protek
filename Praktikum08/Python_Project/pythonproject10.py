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


buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
beliBuah(buah)