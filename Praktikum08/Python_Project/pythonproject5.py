def kuadrat(bil):
    b = []
    a = tuple(bil)
    for i in a:
        i = i ** 2
        b.append(i)
    print("hasil kuadrat =",b)


bil = [2, 4, 5, 6]
kuadrat(bil)