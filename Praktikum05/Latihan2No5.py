from random import randint
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
secret = randint(0, 100)

while True:
    tebak = int(input('Tebakan Anda :'))
    if tebak > secret:
        print('Hehehe… Bilangan tebakan anda terlalu besar')

    elif tebak < secret:
        print('Hehehe… Bilangan tebakan anda terlalu kecil')

    else:
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        break