myString = "python adalah bahasa pemrograman yang menyenangkan"
hurufPenyusun = set(myString)
alfa = list(hurufPenyusun)
urutan = sorted(alfa, key=str.lower)
print(urutan)