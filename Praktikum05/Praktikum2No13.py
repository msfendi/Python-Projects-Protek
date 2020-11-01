hitung = 0
from random import randint
while True:
    hitung = hitung + 1
    bil = randint(0, 10)
    print(bil)
    if bil == 5:
        break
print('Jumlah perulangan :',str(hitung))