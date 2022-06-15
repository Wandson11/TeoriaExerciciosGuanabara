#fazer um programa que alimente uma lista
#depois, criar 2 listas extra, uma para os valores pares, outra para os valores impares
#no final, mostrar as 3 listas.

#resultado deu certo, apliquei a separaçao dos números impares e pares, no ato.

'''lista = []
listapar = []
listaimpar = []
continuar = ''
while continuar != 'N':
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
    continuar = str(input('Desejar continuar? ')).upper()
print(f'Os valores digitados são {lista}')
print(f'Os valores pares são: {listapar}')
print(f'Os valores pares são: {listaimpar}')'''

#parte 2, foi pedido que fizesse a separaçao dos numeros, somente com a primeira lista feita

lista = []
listapar = []
listaimpar = []

while True:
    lista.append(int(input('Digite o valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar in 'nN':
        break
print(f'Os valores são: {lista}')

for c, valor in enumerate(lista):
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
print(f'Os valores pares são {listapar}')
print(f'Os valores impares são {listaimpar}')

#essa segunda resolução ficou identica ao do Guanabara