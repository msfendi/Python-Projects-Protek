import math
print('Aplikasi Tarif Rental Mobil')
print('Daftar Tarif')
tarifsewapertama = 200000
tarifsewaberikutnya = 10000
print('Tarif Sewa 12 Jam Pertama:', tarifsewapertama)
print('Tarif Sewa Berikutnya per-Jam:', tarifsewaberikutnya)
jammasuk = 06.00
jamkeluar = 23.50
jamsewapertama = 12

lamasewaseluruhnya = jamkeluar - jammasuk
lamasewaberikutnya = math.floor(lamasewaseluruhnya - jamsewapertama)
biayasewaberikunya = (lamasewaberikutnya * tarifsewaberikutnya)

totaltarif = tarifsewapertama + biayasewaberikunya
print('Lama sewa mobil:', lamasewaseluruhnya, 'Jam' )
print('Total Tarif: Rp.',totaltarif)

