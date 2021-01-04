from datetime import *
def diffDate(x):
    k = x.split("-")
    tglskrg = datetime.date(datetime.now())
    tgllalu = date(int(k[0]), int(k[1]), int(k[2]))

    selisih = (tglskrg - tgllalu).days
    print(selisih)
try:
    inputtgl = input('Masukkan Tanggal Yang Diinginkan (YYYY-MM-DD) = ')
    diffDate(inputtgl)
except ValueError:
    print("Masukkan Tanggal Sesuai Format")
except IndexError:
    print("Masukkan Tanggal Sesuai Format")