try:
    input_file = input("Masukkan nama file: ")
    file = open(input_file, "a")
    boolean = "y"
    while(boolean == "y"):
        tambah_data = input("Data yang mau ditambahkan: ")
        file.write(tambah_data)
        boolean = input("Mau lagi (y/n) : ",)
    file.close()
except FileNotFoundError:
    print("File tidak ditemukan")
except PermissionError:
    print("Tidak dapat izin untuk mengakses file")