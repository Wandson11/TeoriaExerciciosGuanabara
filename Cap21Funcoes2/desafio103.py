#função chamada ficha(), que recebe dois parametros o nome e qtos gols ele fez.
#o programa deverá mostrar a ficha completa, mesmo que esteja faltando alguma info.
#será preenchido pelo usuário

'''def ficha(a='desconhecido', b=0):
    if a == '':
        a = 'Desconhecido'
    if b == '':
        b = '0'
    print(f'O jogador {a} fez {b} gol(s) no campeonato')

n1 = str(input('Digite o nome do jogador:'))
n2 = str(input('Digite os gols feitos por esse jogador: '))
print(ficha(n1, n2))'''

def ficha(jogo='<desconhecido>', gol=0):
    print(f'O jogador {jogo} fez {gol} gol(s) no campeonato')


n = str(input('Digite o nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

