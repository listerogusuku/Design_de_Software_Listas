def filtra_bagagens(lista_bagagens, altura, largura, profundidade):
    i = 0
    # soma = 0
    geral = 0
    while i < len(lista_bagagens):
        if lista_bagagens[i][0] > altura:
            geral+=1
        elif lista_bagagens[i][1] > largura:
            geral+=1
        elif lista_bagagens[i][2] > profundidade:
            geral+=1
        i+=1
    return geral


bagagens = [[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0], [50.3, 30.2, 30.0], [54.0, 30.2, 22.1]]
altura = 55
largura = 35
profundidade = 25

print(filtra_bagagens(bagagens, altura, largura, profundidade))
