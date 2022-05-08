#escreve um programa que faça o computador "pensar" em um numero interio de 0 a 5 para o usuário tentar adivinhar qual
#o número escolhido.

import random

#esse foi o que eu fiz, está funcional
'''vidente = int(input('Qual foi o número escolhido pelo computador? '))
lista = [0, 1, 2, 3, 4, 5]
aleatorio = random.choice(lista)
if vidente == aleatorio:
    print(f'Parabéns, vc acertou, o número escolhido foi {aleatorio}')
else:
    print(f'vc errou, o número escolhido foi {aleatorio}')'''

#exemplo usado na aula do guanabara
computador = random.randint(0, 5) #numero será o escolhido entre o intervalo dentro dos parenteses
print('-=-' *20)
print('Vou pensar em um número.')
print('-=-' *20)
jogador = int(input('Escreva um número de 0 a 5: '))
if jogador == computador:
    print(f'Parabéns, voce adivinhou o numero {computador}')
else:
    print(f'vc perdeu, pensei em {computador}!')
    
#diferença é que em aula foi usado o randint.
