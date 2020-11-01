from random import randint
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
secret = randint(0, 100)
skor = 100

while True:
    if skor > 0:
        tebak = int(input('Tebakan Anda :'))
        if tebak > secret:
            skor = skor - 2
            print('Hehehe… Bilangan tebakan anda terlalu besar')

        elif tebak < secret:
            skor = skor - 2
            print('Hehehe… Bilangan tebakan anda terlalu kecil')

        else:
            print('Yeeee… Bilangan tebakan anda BENAR :-)')
            break
    else:
        print('Game Over Guys!!!!!!')
        print('Angkannya adalah :', secret)
        break
print(' ')
print('Skor kamu adalah :' ,skor)