#ajude o jogador com palpites na mega sena

'''from random import randint
from time import sleep
loteria = int(input('Quantos jogos voce quer fazer? '))
lista = list()
for c in range(0, loteria):
    for n in range(0, 6):
        jogo = randint(1, 60)
        if jogo not in lista: #aqui, para nao repetir o número em uma lista.
            lista.append(jogo)
    print(f'Jogo {c+1} {lista}')
    sleep(0.5)
    lista.clear()
print(lista)'''

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=-' * 30)
print('        JOGO DA MEGA SENA       ')
print('-=-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot  = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont > 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.4)
print('-=' * 5, f'< BOA SORTE >', '-=' * 5)

#ajsutei o meu modelo, com a resoluçao oficial do Guanabara.
'''from random import randint
from time import sleep
loteria = int(input('Quantos jogos voce quer fazer? '))
lista = list()
principal = list()
for c in range(0, loteria):
    for n in range(0, 6):
        jogo = randint(1, 60)
        if jogo not in lista: #aqui, para nao repetir o número em uma lista.
            lista.append(jogo)
    lista.sort()
    principal.append(lista[:])
    print(f'Jogo {c+1} {lista}')
    sleep(0.5)
    lista.clear()
print(principal)'''
