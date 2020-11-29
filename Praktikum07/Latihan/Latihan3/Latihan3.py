print("-"*30)
print("Program Hitung Rata - Rata")
print("-"*30)

boolean = "y"
pembilang = 0
pembagi = 0
while (boolean == "y"):
    try:
        bil = int(input("Masukkan bilangan bulat :"))
        pembilang += bil
        pembagi += 1
        boolean = input("Lagi (y/n) :")
        if (boolean == "y"):
            boolean = "y"
        elif (boolean == "n"):
            boolean = "n"
        else:
            print("Inputan salah")

    except ValueError:
        print("Bukan bilangan bulat")
        continue

hasil = pembilang/pembagi
print()
print("Rata-ratanya adalah : ", hasil)