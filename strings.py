# def zera_negativos(lista):
#     i = 0
#     while i < len(lista):
#         if lista[i] < 0:
#             lista[i] = 0
#         i+=1
#     return lista



# listinha = [0,10,25,-3,-5,63,-14,10,100,1000]

# print(zera_negativos(listinha))





# while True:
#     palavras = input('Digite palavras: ')
#     if palavras == 'fim':
#         break
#     else:
#         lista = []
#         lista.append(palavras)
#         if lista[0][0] == 'a':
#             print(palavras)



# lista1 = [1,2,3,4]
# lista2 = [10,20,30,40]

# print(lista1+lista2)

# nova_lista = []
# nova_lista.append(lista1)
# nova_lista.append(lista2)
# print(nova_lista)

# print(lista1*len(lista1))





# def conta_a(n):
#     cont = 0
#     soma=0
#     while cont < len(n):
#         if n[cont] == 'a':
#             soma+=1
#         cont+=1
#     return soma


# strings = 'banana nanica'

# print(conta_a(strings))





'''

string_a = 'banana'
string_b = 'nanica'

string_c = '     aaaagoraaa   mais um testee    '

string_d = ['a', 'teste', 'macarrão', 'Insper']

print(string_a+string_b)

print(string_a.find('n'))

print(string_a.replace('a', 'o'))

print(string_c.strip())

print(string_c.replace('     ', ''))

print(string_c.split(','))

print('==>'.join(['a', 'teste', 'macarrão', 'Insper']))

print(''.join(['     aaaagoraaa   mais um testee    ']))

print(','.join(['Lister', 'Ogusuku', 'Ribeiro']))

print(string_a[3:])


'''




# def eh_palindromo(word):
#     if word[::-1] == word:
#         return True
#     else:
#         return False

# print(eh_palindromo('roma é amor'))



# def pos_arroba(email):
#     arroba = email.find('@')
#     return arroba


# print(pos_arroba('youremail@gmail.com'))





# def quantos_uns(n):
#     str(n)
#     n.split(',')
#     lista = []
#     lista.append(n)
#     # lista.split(',')
#     print(lista)
#     valor = lista.count(1)
#     print(valor)
#     return valor


# print(quantos_uns(15978544543))




# def lista_sufixos(string):
#     c = 0
#     nova_lista = []
#     while c < len(string):
#         valor = string[c:]
#         print(valor)
#         nova_lista.append(valor)
#         print(nova_lista)
#         c+=1
#     return nova_lista


# print(lista_sufixos('banana'))


# def lista_sufixos(string):
#     c = 0
#     nova_lista = []
#     while c < len(string):
#         print(nova_lista)
#         valor = string[c:]
#         print(valor)
#         nova_lista.append(valor)
#         print(nova_lista)
#         c+=1
#     return nova_lista


# print(lista_sufixos('banana'))


# numeros = [10.0, 7.6, 8.4, 8.1]

# print(sorted(numeros))

