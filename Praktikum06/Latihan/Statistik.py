# Function SUM
def sum(*myData):
    total = 0
    for data in myData:
        total = total + data
    print('Jumlah nilainya adalah =', total)

# Contoh Soal SUM
sum(1, 0, 0, 2, 4, 3, 5, 6)

print(' ')

# Function Average
def average(*myData):
    total = 0
    i = 0
    for data in myData:
        total = total + data
        i = i + 1

    ratarata = total/i
    print('Jumlah rata-ratanya adalah =', ratarata)

# Contoh Soal Average
average(2, 3, 4, 5, 6)

print(' ')

# Function Maksimum
def maks(*myData):
    maks = 0
    for i in myData:
        if i > maks:
            maks = i
    return maks

# Function Maksimum dengan Max
def makss(*myData):
    maks = max(myData)
    print('Nilai Maksimumnya adalah : :', maks)

# Contoh Soal Nilai Maksimum
print('Nilai Maksimumnya adalah :', maks(6,12,18,76,54,98,65,1))

print(' ')

# Function Minimum
def mins(*myData):
    min = 99
    for i in myData:
        if i < min:
            min = i
    return min

# Function Minimum dengan Min
def mines(*myData):
    mines = min(myData)
    print('Nilai Minimumnya adalah : :', mines)

# Contoh Soal Nilai Minimum
print('Nilai Minimumnya adalah :', mins(6,12,18,76,54,98,65,1))