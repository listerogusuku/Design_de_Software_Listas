# def alerta(x, y, z, r):
#     if x < r or y < r or z < r:
#         return True
#     else:
#         return False





def alerta(lista, r):
    if lista[0] < r or lista[1] < r or lista[2] < r:
        return True
    else:
        return False


coordenadas = [10,10,10]
raio = 10

print(alerta(coordenadas, raio))