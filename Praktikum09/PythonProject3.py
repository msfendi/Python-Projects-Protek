# Program startFormation1
def starFormation1(n):
    kolom = 1

    i = 0
    while (i <= n):
        bintang = "*" * kolom
        print(bintang.center(10))
        i += 1
        kolom += 2

# Program startFormation2
def starFormation2(n):
    kolom = n + 1

    i = 0
    while (i < n):
        bintang = "*" * kolom
        print(bintang.center(10))
        i += 1
        kolom -= 2

# Program startFormation3
def starFormation3(n):
    k = round(n/2)
    starFormation1(n-k)
    starFormation2(k)

# Output startFormation3
print('Formasi Bintang Center startFormation3 :')
starFormation3(7)