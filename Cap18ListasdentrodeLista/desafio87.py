#igual ao 86, fazendo uma matriz 3 x 3, mas com as seguintes informaçoes:
#a soma de todos os valores pares digitados;
#a soma dos valores presentes na terceiro coluna
#o maior valor da segunda linha

#nao está separando o maior da linha dois.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #se deixar vazio, sem o zeros, dá erro no input
par = []
somapar = terceiracoluna = maior = 0

for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor da matriz [{l} {c}] '))
        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
            somapar += matriz[l][c]
        if c == 2:
            terceiracoluna += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end = ' ')
    print()
print(par)
print(f'A soma dos valores pares é de {somapar}')
print(f'A soma dos valores da terceira coluna é de {terceiracoluna}')
print(maior)

#Guanabara
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor: [{l} {c}]'))
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=-' * 30)
print(f'A soma dos valores pares é de {spar}')
for l in range(0, 3):
    scol += matriz[l][2] #ao inves de colocar o if, como fiz, já mandou direito o scol limitando na terceira coluna
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')'''