sayur = ["bayam", "kangkung", "wortel", "selada"]

def tambah():
    a = input("Masukkan data sayur =")
    sayur.append(a)

def hapus():
    b = input("Data yang dihapus =")
    if(b in sayur):
        sayur.remove(b)
    else:
        print("Sayur tidak ditemukan")

def tampil():
    print(sayur)


while True:
    print("Pilihan Menu :")
    print("A. Tambah data sayur")
    print("B. Hapus data sayur")
    print("C. Tampilkan data sayur")
    print("D. Keluar")
    print()
    menu = input("Pilih Menu =")
    if(menu == "A" or menu == "a"):
        tambah()
    elif(menu == "B" or menu == "b"):
        hapus()
    elif(menu == "C" or menu == "c"):
        tampil()
    elif(menu == "D" or menu == "d"):
        print("Terima kasih")
        break
    else:
        print("Masukkan pilihan dengan benar")
        continue