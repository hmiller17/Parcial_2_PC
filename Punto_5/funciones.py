def mediana(lista):
    lista.sort()
    a = len(lista)//2
    if (a / 2 == int):
        print(lista[a-1],lista[a])
    else:
        print(lista[a])