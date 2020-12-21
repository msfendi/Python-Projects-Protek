mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

list = []

print(70 * '=')
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(25), "TGL LAHIR".ljust(18), "TEMPAT LAHIR".ljust(20))
print(70 * '-')

for i in mhs:
    a = i.split(':')
    list.append(a)

for i in list:
    b = i[2].split('-')
    b.reverse()
    tanggal = '/'.join(b)

    print(i[0].ljust(10), i[1].ljust(25), tanggal.ljust(18), i[3].ljust(20))

print(70 * '-')