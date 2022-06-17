#fazer uma matriz 3x3, que recebe 9 números digitados pelo usuário.

'''lista = [[], [], []]
final = []
for c in range(0, 3):
    for p in range(0, 3):
        teste = int(input(f'Digite um valor para [{c}, {p}]: '))
        if c == 0:
            lista[0].append(teste)
        elif c == 1:
            lista[1].append(teste)
        else:
            lista[2].append(teste)
print(lista[0])
print(lista[1])
print(lista[2])'''

#Guanabara

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]#declara, logo de cara, os valores da matriz, onde serão substituido

#for de alimentação
for l in range(0, 3): #especificando o número de linhas
    for c in range(0, 3): #especificando o número de colunas.
        matriz[l][c] = int(input(f'Digite um valor: [{l} {c}]'))
print('-=-' * 30)
#daqui pra baixo, é a estruturaçao de repetição, para mostrar o resultado na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()#quebrar a linha