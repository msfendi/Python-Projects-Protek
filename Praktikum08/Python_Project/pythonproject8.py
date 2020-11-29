def rataHarga1(buah):
    totalharga = 0
    jumlahharga =0
    harga = list(buah.values())
    for i in harga:
        totalharga += i
        jumlahharga += 1

    rata = totalharga / jumlahharga
    print(rata)

buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
rataHarga1(buah)

# ==========================================================================

def rataHarga2(buah):
    harga = list(buah.values())
    rata = sum(harga) / len(harga)
    print(rata)


buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
rataHarga2(buah)