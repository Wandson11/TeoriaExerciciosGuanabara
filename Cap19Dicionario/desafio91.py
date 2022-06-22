#4 jogadores, jogam um dado, com resultados aleatórios.
#Guardar os resultados em um dicionário.
#No fim, ordenar em ordem crescente e o vencedor, tirou o maior número.

'''from random import randint
from time import sleep
jogadores = dict()
total = []
for c in range(1, 5):
    jogadores['jogador'] = randint(1, 6)
    print(f'O jogador {c} tirou {jogadores["jogador"]}')
    #total.append(jogadores.copy())
#print(total)
print('Ranking dos jogadores')
for k, v in jogadores.items():
    if total[0]:
        maior
    print(f'{k} {v}')'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-=' * 25)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.3)
