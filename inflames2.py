def calcula_cm(lista1, lista2):
    i = 0
    soma = 0
    somay = 0
    if lista1 == [] or lista2 == []:
        return []
    else:
        while i < len(lista1):
            soma += lista1[i]
            xcm = soma/len(lista1)
            somay += lista2[i]
            ycm = somay/len(lista2)
            i+=1
        lista_final = []
        lista_final.append(xcm)
        lista_final.append(ycm)
        return lista_final

entrada1 = [1,1,1,1]
entrada2 = [0,0,0,0]

print(calcula_cm(entrada1,entrada2))

