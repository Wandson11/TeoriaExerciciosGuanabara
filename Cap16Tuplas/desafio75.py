#digitar 4 números e guarda-los em uma tupla.
#responda: qtos n. 9 apareceram; em que posicaçao foi digitado n.3; quais sao pares
# se 3 nao for digitado, tem que aparecer "nao foi digitado em nenhuma posição".

#usar mesma ideia do 74, valores ja dentro da tupla
'''numeros = (int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
print(f'Os valores digitados foram: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vez(es)')
if numeros.count(3):
    print(f'O numero 3 foi digitado na casa {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('Os números par(es) digitados são: ', end = ' ')
for c in numeros: # isso daqui peguei nos comentários.
    if c % 2 == 0:
        print(f'{c}', end= ' ')'''

#guanabara

núm = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+ 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end = ' ')
for n in núm:
    if n % 2 == 0:
        print(n, end = ' ')

