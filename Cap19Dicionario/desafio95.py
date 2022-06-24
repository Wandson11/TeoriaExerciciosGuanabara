#igual ao 93, com nome do jogador, partidas jogadas e gols feitos.
#funcionar com mais jogadores.
#visualização de detalhes de aproveitamento

'''registro = dict()
listadosgols = list()
listona = []
while True:
    registro.clear()
    listadosgols.clear()
    registro['nome'] = str(input('Nome: '))
    partida = int(input(f'Quantas partidas {registro["nome"]} jogou? '))
    for c in range(1, partida + 1):
        listadosgols.append(int(input(f'Quantos gols na partida {c}? ')))
    registro['gols'] = listadosgols[:]
    registro['totalgols'] = sum(listadosgols)
    listona.append(registro.copy())
    while True:
        continuar = str(input('Deseja continuar cadastrando jogadores? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('Erro, digite somente S ou N')
    if continuar in 'N':
        break

print(listona)
print(f'{"No.":<4} {"Nome":<10} {"Gols":<15} {"Total":>4} ')
for c in range(0, len(listona)):
    print(f'{c}    {listona[c]["nome"]}     {listona[c]["gols"]}       {listona[c]["totalgols"]}')

while True:
    maisinfo = int(input('Mostrar dados de qual jogador?[999 para sair] '))
    if maisinfo == 999:
        print('Finalizado o cadastro')
        break
    if maisinfo <= len(listona) - 1:
        print(f'Levantamento do jogador {listona[maisinfo]["nome"]}')
        for k, v in enumerate(registro["gols"]):
            print(f'Na partida {k}, foi feito {v} gol(s)')'''
time = []
jogador=dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'SN':
            break
        print('ERRO. Responda com somente S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()

print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3 }', end=' ')
    for d in v.values():
        print(f'{str(d):<15}')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO, nao existe esse número cadastrado.')
    else:
        print(f'----LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, v in enumerate(time[busca]["nome"]):
            print(f'    No jogo {i+1} fez {v} gol(s)')
    print('-=' * 30)
print('<<<VOLTE SEMPRE>>>')


