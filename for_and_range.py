# n = 10

# for cont in range(n):
#     print(cont)



# num = int(input('Digite um número para iniciar sua lista de pares: '))
# num2 = int(input('Digite um número para ser o último da sua lista de pares: '))

# for i in range(num, num2+1):
#     if i % 2 == 0:
#         print(i)



# for i in range(num, num2+1, 2):
#     print(i)


#Modeling of a lançamento de um foguete:

# print('\nLançamento!\n')
# for i in range(10, 0, -1):
#     print(f'Contagem regressiva: {i}')
# print('\nFoguete lançado!\n')


'''

RANGE ==> (começo, != fim, valor de incremento)


'''


# n = int(input('Digite a fatorial desejada: '))

# c = 1
# for i in range(n, 1, -1):
#     c*=i

# print(f'O fatorial de {n} é {c}.')


# n = 5

# for n in range(5, 51, 5):
#     print(n*(n+1)//2)

'''


total = int(input('\nQual o número total de eleitores? '))

candidatoA = 0
candidatoB = 0
candidatoC = 0

for i in range(total):
    voto = int(input('Em quem você deseja votar? [1 - CandidatoA, 2 - Candidato B, 3- Candidato C:] '))
    while True:
        if voto > 3 or voto < 1:
            voto = int(input('Voto inválido! Digite um valor válido entre 1 e 3!'))
        else:
            break
    if voto == 1:
        candidatoA+=1
    elif voto == 2:
        candidatoB+=1
    else:
        candidatoC+=1
    
print('\n Votação encerrada! \n')

print('\nApuração dos votos:\n')

print(f'Quantidade de votos do candidato A: {candidatoA} votos.')
print(f'Quantidade de votos do candidato B: {candidatoB} votos.')
print(f'Quantidade de votos do candidato C: {candidatoC} votos.')

print('\nObrigado por participar dessa eleição!\n')

'''



# for i in range(3):
#     for j in range(3):
#         print(i, j)

# for j in range(3):
#     for i in range(3):
#         print(j, i)



# start = int(input('Digite o número inicial da tabuada: '))
# end = int(input('Digite o valor final da tabuada: '))


# for i in range(start, end+1):
#     print(f'\nPara a tabuada do {i}:\n')
#     for j in range(start, end+1):
#         print(f'{i} x {j} = {i*j}')





# n = int(input('Digite o número de sequências: '))

# for i in range(n):
#     print(f'Sequência {i+1}')
#     num = int(input('Digite um número da sequência: '))
#     soma = 0
#     while num != 0:
#         if num % 2 == 0:
#             soma += num
#         num = int(input('Digite um número da sequência: '))
#     print(f'\nA soma da sequência {i+1} é {soma}.')



# n1 = int(input('Digite um número inteiro: '))
# n2 = int(input('Digite o segundo número inteiro: '))

# r1 = float(input('Digite um número real: '))

# print(f'O dobro de {n1} com metade de {n2} é {(n1*2)*(n2/2)}')
# print(f'{(n1*3)+r1}')
# print(f'{r1**3}')



# print(int(5.4)) #converte float para inteiro



'''
num = float(input('Digite um número: '))

if num != int(num):
    print(f'{num} é decimal!')
    fracao = num - int(num)
    new_num = num
    if fracao >= 0.5:
        new_num+=1
    print(f'{num} arredondado equivale a {int(new_num)}')
else:
    print(f'{num} é inteiro')

'''

# numero = float(input('Digite um número: '))

# print(f'O número que você digitou equivale, ao ser arredondado, a: {round(numero)}')


import math

# print(math.sin(1))
# print(math.sqrt(4))


# def aproxima_raiz(x):
#     math.pow(x, 2)
#     return x

# a = float(input('Digite o valor que você deseja ver a raiz aproximada: '))

# print(aproxima_raiz(a))



# print(math.pow(16, 2))

# print(list(range(21)))









import random

# random.randrange(start, stop[, step]) #NÃO CONTA o valor b

# for i in range(10):
#     # x = random.randrange(1,7) #sorteia números aleatórios entre 1 e 7, sem contar o 7 efetivamente
#     x = random.randrange(1,7,2) #sorteia números aleatórios de 1 até 7 com passo 2, ou seja, só sorteará entre 1, 3 e 5
#     print(x)





#random.randint(a, b) #número inteiro entre a e b, porém CONTANDO O B

# for i in range(10):
#     x = random.randint(1, 7)
#     print(x)




#O random.choice simplesmente pega o valor que desejarmos ficar brincando e vai substituindo ele
#Retorna um elemento aleatório de uma sequência não vazia

# for i in range(10):
#     x = random.choice([10, 20, 30]) #Equivalente a random.choice(range(1, 7))
#     print(x)



#random.random()
#Retorna um real entre 0 e 1


#Exemplo:

# for i in range(10):
#     print(random.random()) #Vai simplesmente ficar sorteando e escolher um número REAL entre zero e 1 (nesse caso)


# for i in range(10):
#     x = random.uniform(1, 7) #Vai retornar um número real entre os reais 1 e 7
#     print(x)



# lista = list(range(1, 21, 2))

# for i in range(10):
#     print(lista[i])




# lista = list(range(10))

# print(lista[2:10])


# print(lista[0:10:2])

# print(lista[::-3])


# lista = [1,2,3,4, [10,20,30,40]]

# print(lista[4][2])


# lista2 = [[[1,2], [3,4]], [5,6]]

# print(lista2[0])


# lista = []

# for i in range(0,7):
#     x = int(input(f'Digite um número {i}: '))
#     lista.append(x)

# print(lista)



# lista_notas = []

# soma = 0
# for i in range(4):
#     notas = float(input(f'Digite a nota {i}: '))
#     soma+=notas
#     lista_notas.append(notas)

# print(f'As notas foram: {lista_notas} e a média do aluno foi {soma/len(lista_notas)}')


'''
lista_inteiros = []

lista_pares = []
lista_impares = []
for i in range(5):
    num = int(input('Digite um número inteiro: '))
    lista_inteiros.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(f'\nA lista de números digitados por você foi: {lista_inteiros}\n')
print(f'A lista de números pares é: {lista_pares}\n')
print(f'A lista de números ímpares é: {lista_impares}')

'''

# lista = []

# n = float(input('Digite um número a ser adicionado à lista: '))
# while n != -1:
#     lista.append(n)
#     n = float(input('Digite um número a ser adicionado à lista: '))

# elemento = float(input('Digite o número que você deseja procurar na lista: '))

# cont=0
# for i in range(len(lista)):
#     if lista[i] == elemento:
#         cont+=1

# print(f'O elemento {elemento} apareceu um total de {cont} vezes na lista.')





# n = int(input('Digite o número que você deseja ver o fatorial: '))

# c = 1
# fatorial = 1

# while c <= n:
#     fatorial*=c
#     c+=1

# print(fatorial)



# def fatorial(n):
#     c = 1
#     fatorial = 1

#     while c <= n:
#         fatorial*=c
#         c+=1
#     return fatorial

# print(fatorial(5))


# while True:
#     palavra = input('Digite uma palavra:')
#     if palavra == 'desisto':
#         break
# print('Você acertou a senha!')




# def calcula_euler(x,n):
#     soma = 1



# def raiz_quadrada(x):
#     cont = 0
#     impar = 1
#     while cont <= x:
#         x = x - impar
#         impar+=2
#         cont+=1



# x = int(input('Digite o número que você deseja ver a raiz: '))
# cont = 0
# impar = 1
# lista_geral = []
# while cont <= x:
#     lista_geral.append(impar)
#     x = x - impar
#     impar+=2
#     cont+=1

# print(len(lista_geral))




'''
def raiz_quadrada(x):
    cont = 0
    impar = 1
    while cont <= x:
        if x == 0:
            break
        x = x - impar
        impar+=2
        cont+=1
    return cont
'''


'''
n = 0
result = 0
while n<99:
    result += (1 / (2**n))
    print(result)
    n += 1
    print(n)

print(result)
'''


# n = int(input('Digite um número: '))

# cont = 0
# fatorial = 1
# x = 1

# while cont < n:

#     fatorial *= n

#     x += ((x**n) / fatorial )

#     n+=1





'''
def calcula_euler(x, n):
    cont = 0
    fatorial = 1
    result = 0
    final = 0

    while cont < n:
        c = 1
        fatorial = 1
        while c <= n:
            fatorial*=c
            c+=1

        # fatorial *= n
        result += ((x**n) / fatorial )

        print(result)

        n+=1
        cont+=1

        final = 1+result

        return final


print(calcula_euler(2,3))

'''







# def fatorial(n):
    # c = 1
    # fatorial = 1

    # while c <= n:
    #     fatorial*=c
    #     c+=1
    # return fatorial

# print(fatorial(5))



'''
def calcula_euler(x, n):
    cont = 0
    fatorial = 1
    result = 0
    final = 0

    while cont < n:
        c = 1
        fatorial = 1
        while c <= n:
            guarda_fat = fatorial
            fatorial*=c
            result += ((x**n) / fatorial )
            n+=1
            cont+=1
            fatorial = guarda_fat
            fatorial+=1
            c+=1

        n+=1
        cont+=1

        final = 1+result

        return final


print(calcula_euler(2,3))
'''


# def quantos_uns(x):
#     return 'x'.count('1')


# x = 10391019281

# x.count('1')

# print(x)

# a = 19872131

# print(quantos_uns(str(a)))


# print('33445566849'.count('3'))


# def quantos_uns(x):
#     y = 0
#     if x:
#         if x[0] == '1':
#             y += 1
#         y += quantos_uns(x[1:])
#     return y

# print(quantos_uns('1232421111'))



# def junta_nome_sobrenome(x,y):
#     nova_lista = []
#     nova_lista.append(x)
#     nova_lista.append(y)
#     return nova_lista


# a = ['Lister']
# b = ['Ogusuku']

# print(junta_nome_sobrenome(a, b))

