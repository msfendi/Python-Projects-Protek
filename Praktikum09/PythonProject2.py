# Program startFormation1
def starFormation1(n):
    kolom = 1

    i = 0
    while (i < n):
        bintang = "*" * kolom
        print(bintang.center(10))
        i += 1
        kolom += 2

# Output startFormation1
print('Formasi Bintang Center startFormation1 :')
starFormation1(4)