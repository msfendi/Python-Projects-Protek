try:
    file = open("E:/FENDI/SEKOLAH/Kuliah/SEMESTER 1/PEMROGRAMAN TERSTRUKTUR/Python Projects/Python-Projects-Protek/Praktikum07/Praktikum3/data.txt")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print("Tidak dapat mengubah huruf menjadi integer")