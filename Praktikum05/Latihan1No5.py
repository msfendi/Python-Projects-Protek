kodekaryawan = input('Masukkan Kode Karyawan = ')
namakaryawan = input('Masukkan nama karyawan = ')
golongan = input('Masukkan Golongan (A/B/C/D) = ')
status = input('Masukkan Status (1:Menikah, 2:Belum) = ')
if(status == '1'):
    statusMenikah = 'Sudah Menikah'
    persentaseTunjanganIstriSuami = 10/100
    anak = int(input('Masukkan Jumlah Anak = '))
    persentasetunjanganAnak = 5/100 * anak
else:
    statusMenikah = 'Belum'
    persentaseTunjanganIstriSuami = 0
    anak = 0
    persentasetunjanganAnak = 0


if(golongan == 'A'):
    gp = 10000000
    potongan = 2.5/100
    tunjanganSuamiIstri = persentaseTunjanganIstriSuami * gp
    tunjanganAnak = persentasetunjanganAnak * gp
    gk = gp + tunjanganSuamiIstri + tunjanganAnak
    nilaiPotongan = gk * potongan
    gb = gk - nilaiPotongan
elif(golongan == 'B'):
    gp = 8500000
    potongan = 2.0/100
    tunjanganSuamiIstri = persentaseTunjanganIstriSuami * gp
    tunjanganAnak = persentasetunjanganAnak * gp
    gk = gp + tunjanganSuamiIstri + tunjanganAnak
    nilaiPotongan = gk * potongan
    gb = gk - nilaiPotongan
elif(golongan == 'C'):
    gp = 7000000
    potongan = 1.5/100
    tunjanganSuamiIstri = persentaseTunjanganIstriSuami * gp
    tunjanganAnak = persentasetunjanganAnak * gp
    gk = gp + tunjanganSuamiIstri + tunjanganAnak
    nilaiPotongan = gk * potongan
    gb = gk - nilaiPotongan
elif(golongan == 'D'):
    gp = 5500000
    potongan = 1.0/100
    tunjanganSuamiIstri = persentaseTunjanganIstriSuami * gp
    tunjanganAnak = persentasetunjanganAnak * gp
    gk = gp + tunjanganSuamiIstri + tunjanganAnak
    nilaiPotongan = gk * potongan
    gb = gk - nilaiPotongan

print('=' * 50)
print('STRUK RINCIAN GAJI KARYAWAN')
print('-' * 50)
print('Nama Karyawan :', str(namakaryawan), '(', kodekaryawan, ')')
print('Golongan :', golongan)
print('Status Menikah :', str(statusMenikah))
print('Jumlah Anak :', str(anak))
print('-' * 50)
print('Gaji Pokok : Rp.', gp)
print('Tunjangan Istri/Suami : Rp.', tunjanganSuamiIstri)
print('Tunjangan Anak : Rp.', tunjanganAnak)
print('-' * 50)
print('Gaji Kotor : Rp.', gk)
print('Potongan : Rp.', nilaiPotongan)
print('-' * 50)
print('Gaji Bersih : Rp.', gb)