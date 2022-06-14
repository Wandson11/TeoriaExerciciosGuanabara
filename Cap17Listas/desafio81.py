#programa que incluia vários números em uma lista.
#qts nº foram digitados; lista de valores em sua forma decrescente
#se 5 foi digitado

'''lista = []
continuar = ''
cont = 0

while continuar != 'N':
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    cont +=1
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()

lista.sort(reverse=True)
print(f'Foram digitados {cont} vezes')
print(f'a lista ficou assim: {lista}')
if 5 in lista:
    print(f'O valor 5 está presente na lista')
else:
    print('O valor 5 não foi digitado')'''

#Guanabara
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]:'))
    if resp in 'Nn':
        break
print('-=-' * 30)
print(f'Voce digitou {len(valores)} elementos') # aqui, nao usou o contador mas sim, o len.
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrada na lista.')