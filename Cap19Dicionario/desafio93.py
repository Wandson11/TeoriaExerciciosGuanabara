#programa que leia o nome do jogar e o número de partidas jogadas
#juntamente com os gols marcados
#no final, dicionário terá 3 elementos: nome, gols (que será uma lista) e total de gols

'''lista = []
contgol = 0
contjogos = 0
registro = dict()
registro['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantos jogos {registro["nome"]} participou? '))
for c in range(1, jogos+1):
    artilharia = int(input(f'Quanto(s) gol(s) na partida {c}? '))
    lista.append(artilharia)
    contgol += artilharia
    contjogos += 1
registro['gols'] = lista
registro['total'] = contgol
print('-=' * 20)
print(registro)
print('-=' * 20)
for k, v in registro.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {registro["nome"]} jogou {contjogos} partidas')
for c in range(0, jogos ):
    print(f'=> Na partida {c+1}, fez {registro["gols"][c]} gol(s)')'''

jogador=dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
