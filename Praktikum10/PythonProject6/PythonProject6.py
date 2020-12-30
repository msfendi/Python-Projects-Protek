try:
    teks = input('Masukkan Text = ')
    lompat = int(input('Lompatan = '))
    listtext = list(teks)
    listbaru = []

    for i in listtext:
        if (i != ' '):
            ordhuruf = ord(i)
            ordtotal = int(ordhuruf + lompat)
            if (ordtotal > 122):
                plus = ordtotal - 122
                ordbaru = 96 + plus
                chrbaru = chr(ordbaru)
                listbaru.append(chrbaru)
            else:
                chrbaru = chr(ordtotal)
                listbaru.append(chrbaru)

        elif (i == ' '):
            listbaru.append(i)


    hasil = ''.join(listbaru)
    print('Teks Sandi : ',hasil.upper())

    filehasil = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject6/hasil.txt', 'w')
    filehasil.write('Teks Sandi : '+hasil.upper())
    filehasil.close()
except ValueError:
    print('Lompatan harus angka')