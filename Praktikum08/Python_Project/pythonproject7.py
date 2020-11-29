def harga(buah):
    key = list(buah.keys())
    value = list(buah.values())
    o = max(buah.values())
    print(key[value.index(o)])

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
harga(buah)