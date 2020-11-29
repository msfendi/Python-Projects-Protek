def beliBuah(buah):
    key = list(buah.keys())
    value = list(buah.values())
    while True:
        a = input("masukkan nama buah = ")
        key = buah.keys()

        if(a not in key):
            print("buah tidak ditemukan")
            continue
        else:
            while True:
                try:
                    jumlah = int(input("masukkan kg = "))
                    i = buah.get(a)
                    totalHarga = i * jumlah
                    print("-" * 20)
                    print("Total Harga : ", totalHarga)
                    break

                except ValueError:
                    print("masukkan nilai dengan benar")
                    continue
        break


buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
beliBuah(buah)
