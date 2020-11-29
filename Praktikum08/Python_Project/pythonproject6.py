def sortStringByChar(buah):
    list1 = []
    for i in reversed(sorted(buah, key=len)):
        list1.append(i)
    print(list1)


buah = ['apel', 'rambutan', 'jeruk ', 'belimbing']
sortStringByChar(buah)