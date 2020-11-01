kodekaryawan = input('Masukkan Kode Karyawan = ')
namakaryawan = input('Masukkan nama karyawan = ')
golongan = input('Masukkan Golongan (A/B/C/D) = ')


if(golongan == 'A'):
    gp = 10000000
    potongan = 2.5/100
    nilaiPotongan = gp * potongan
    gb = gp - nilaiPotongan
elif(golongan == 'B'):
    gp = 8500000
    potongan = 2.0/100
    nilaiPotongan = gp * potongan
    gb = gp - nilaiPotongan
elif(golongan == 'C'):
    gp = 7000000
    potongan = 1.5/100
    nilaiPotongan = gp * potongan
    gb = gp - nilaiPotongan
elif(golongan == 'D'):
    gp = 5500000
    potongan = 1.0/100
    nilaiPotongan = gp * potongan
    gb = gp - nilaiPotongan

print('=' * 50)
print('STRUK RINCIAN GAJI KARYAWAN')
print('-' * 50)
print('Nama Karyawan :', str(namakaryawan), '(', kodekaryawan, ')')
print('Golongan :', golongan)
print('-' * 50)
print('Gaji Pokok : Rp.', gp)
print('Potongan : Rp.', nilaiPotongan)
print('-' * 50)
print('Gaji Bersih : Rp.', gb)