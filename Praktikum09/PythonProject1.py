def ubahHuruf(teks, a, b):
    list_kata = list(teks)
    for i in list_kata:
        if (i == a):
            posisi = list_kata.index(i)
            list_kata.insert(posisi, b)
            list_kata.remove(i)
        else:
            continue

    gabung = ''.join(list_kata)
    print(gabung)


kata = input("Masukkan kata = ")
hurufDiganti = input("Huruf Yang Diganti = ")
hurufPengganti = input("Huruf Pengganti = ")
ubahHuruf(kata, hurufDiganti, hurufPengganti)