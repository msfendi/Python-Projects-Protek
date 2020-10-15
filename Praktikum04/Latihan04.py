#Menghitung Waktu dari Kota A ke B
jarakKotaAkeB = 125
kecepatanAkeB = 62
waktuAkeB = round(jarakKotaAkeB / kecepatanAkeB)
print('Waktu dari Kota A ke B : ', waktuAkeB, 'jam')

#Menghitung Waktu dari Kota B ke C
jarakKotaBkeC = 256
kecepatanBkeC = 70
waktuBkeC = round(jarakKotaBkeC / kecepatanBkeC)
print('Waktu dari Kota B ke C : ', waktuBkeC, 'jam')

print('Waktu istirahat di kota B: 45 menit')

#Proses
waktuIstirahat = 0.45
jamBerangkat = 06.00

waktuPerjalanan = (waktuAkeB + waktuBkeC)
lamaPerjalanan = (waktuPerjalanan + waktuIstirahat)
print('Jam Berangkat: 06.00')
print('Lama Perjalan adalah:', lamaPerjalanan, 'jam')
jamSampai = jamBerangkat + lamaPerjalanan
print('Jadi Pak Amir akan sampai di kota C pada pukul',jamSampai)