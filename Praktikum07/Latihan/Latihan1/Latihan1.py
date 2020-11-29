try:
    input_file = input("Masukkan nama file: ")
    file = open(input_file, "r")
    print("Isi file", input_file, "adalah: ")
    print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan atau kesalahan penulisan")
except PermissionError:
    print("Tidak dapat izin untuk mengakses file")