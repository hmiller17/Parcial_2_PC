def existenciaItem(lista):
    
    for i  in lista:
        j = lista.count(i)
        if(j > 1):
            print("Hay elementos repetidos en la lista")
            break
        else:
            next
    
    if(j == 1):
        print("No hay elementos repetidos en la lista")