def dataStat(x):
    rata = sum(x) / len(x)
    Min = min(x)
    Max = max(x)
    list_hasil = [rata, Max, Min]
    print(list_hasil)

list = [4, 8, 6, 2]
dataStat(list)