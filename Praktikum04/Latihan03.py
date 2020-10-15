import math
jarakKota = 795
jarakTempuh = 12
kapasitasTangki = 50
bensinYangDiperlukan = math.floor(jarakKota / jarakTempuh)
print('Kapasitas tangki:',kapasitasTangki,'Liter')
print('Bensin yang dibutuhkan:',bensinYangDiperlukan,'Liter')

minimalIsi = bensinYangDiperlukan // kapasitasTangki
print('Minimal pengisian bensin:',minimalIsi, 'kali')
