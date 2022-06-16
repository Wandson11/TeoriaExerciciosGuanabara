#escrever 7 números, que serao armazenados dentro de uma lista
#cada número, deve ser identificado entre par ou impar, e ser inserido em uma das duas listas
#assim, existirá uma lista geral, com duas listas dentro
#uma de par outra de ímpar.
'''lista = []
par = []
impar = []
final = []
for c in range(0, 7):
    teste = int(input('Digite um valor: '))
    if teste % 2 == 0:
        par.append(teste)
        lista.append(par[:])
    else:
        impar.append(teste)
        lista.append(impar[:])

lista.sort()
print(lista)'''

#guanabara
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm.sort()
print(f'Todos os valores {núm}')
núm[0].sort()
print(f'Os valores pares digitados: {núm[0]}')
núm[1].sort()
print(f'Os valores ímpares digitados: {núm[1]}')
