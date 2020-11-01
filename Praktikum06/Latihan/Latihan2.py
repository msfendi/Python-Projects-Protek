# Program startFormation1
def starFormation1(n):
    kolom = 0

    i = 0
    while (i < n):
        j = 0
        while (j <= kolom):
            print('* ', end='')
            j += 1
        print('')
        i += 1
        kolom += 1

# Output startFormation1
print('Formasi Bintang startFormation1 :')
starFormation1(4)

print('')

# Program startFormation2
def starFormation2(n):
    kolom = 0

    i = 0
    while (i < n):
        j = n-1
        while (j >= kolom):
            print('* ', end='')
            j -= 1
        print('')
        i += 1
        kolom += 1

# Output startFormation1
print('Formasi Bintang startFormation2 :')
starFormation2(4)

# Program startFormation3
def starFormation3(n):
    k = round(n/2)
    starFormation1(k)
    starFormation2(n-k)

# Output startFormation3
print('Formasi Bintang startFormation3 :')
starFormation3(7)