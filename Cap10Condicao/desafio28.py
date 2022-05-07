#escreve um programa que faça o computador "pensar" em um numero interio de 0 a 5 para o usuário tentar adivinhar qual
#o número escolhido.

import random

vidente = int(input('Qual foi o número escolhido pelo computador? '))
lista = [0, 1, 2, 3, 4, 5]
aleatorio = random.choice(lista)
if vidente == aleatorio:
    print(f'Parabéns, vc acertou, o número escolhido foi {aleatorio}')
else:
    print(f'vc errou, o número escolhido foi {aleatorio}')