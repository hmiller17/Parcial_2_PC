def comparacion(lista1,lista2):
    lista_unica = []
    if(len(lista1) >= len(lista2)):
        lista_mayor = lista1
        lista_menor = lista2
    else:
        lista_mayor = lista2
        lista_menor = lista1
    for i in lista_mayor:
        if(i not in lista_menor):
            lista_unica.append(i)
        else:
            next
    print(lista_unica)
    