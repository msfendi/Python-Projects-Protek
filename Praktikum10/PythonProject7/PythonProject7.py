try:
    teks = input('Masukkan Text = ')
    lompat = int(input('Lompatan = '))
    listtext = list(teks)
    listbaru = []

    for i in listtext:
        if (i != ' '):
            ordhuruf = ord(i)
            minus = int(ordhuruf - lompat)
            if (minus < 96):
                sisa = 97 - minus
                ordasli = 123 - sisa
                chrasli = chr(ordasli)
                listbaru.append(chrasli)
            else:
                chrasli = chr(minus)
                listbaru.append(chrasli)

        elif (i == ' '):
            listbaru.append(i)


    hasil = ''.join(listbaru)
    print('Teks Asli : ',hasil.upper())

    filehasil = open('E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum10/PythonProject7/hasil.txt', 'w')
    filehasil.write('Teks Asli : '+hasil.upper())
    filehasil.close()

except ValueError:
    print('Lompatan harus angka')