import random
def shuffleString(x, n):
    list = []
    for i in range(n):
        shuffle = ''.join(random.sample(x,len(x)))

        if(shuffle in list):
            continue
        else:
            list.append(shuffle)

    print(list)

kata = input("Masukkan Kata : ")
banyak = int(input("Banyak Pengacakan : "))
shuffleString(kata, banyak)