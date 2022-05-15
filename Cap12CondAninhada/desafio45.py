# cria a brincadeira do jo-ken-pô
'''print('Escolha uma das opçoes:
[0] Pedra
[1] Papel
[2] Tesoura')'''

'''mao = int(input('Escolha: '))
print('-=-' * 20)
print('''
#Jo
#ken
#Pô''')
'''import random
lista = [0, 1, 2]
resultado = random.choice(lista)
if mao == 0 and resultado == 2 or mao == 1 and resultado == 0 or mao == 3 and resultado == 1:
    print(f'Você ganhou, sua opçao foi {mao} e o da maquina foi {resultado}')
elif mao == 0 and resultado == 1 or mao == 1 and resultado == 2 or mao == 2 and resultado == 0:
    print(f'Você perdeu, tu jogou {mao} e a máquina jogou {resultado}')
else:
    print(f'Ficou empatado, você jogou {mao} e a máquina também jogou {resultado}')'''

#nesse caso, estava funcional mas nao consegui substituir os 3 numeros pelos nomes, assim, fui ver a aula para consultar a resoluçao.

#resoluçao da aula, usei choice, foi usado na resoluçao do guanabara o randint

from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=-' * 10)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=-' * 10)
#print(f'o computador escolheu {itens[computador]}')
#nesse comnetário de cima, é importante apontar que, inicialmente dentro da chave {computador}, respondia somente os numeros de 0 2.
#porém, colocando o itens e a variavel computador dentro do itens como se fosse uma lista, o programa apresenta os nomes: pedra, papel, tesoura.
if computador == 0: #pc jogou pedra
    if jogador == 0:
        print(f'Deu empate')
    elif jogador == 1:
        print(f'Jogador ganhou, pois colocou {itens[jogador]} e o pc {itens[computador]}')
    elif jogador == 2:
        print(f'O computador ganhou, pois colocou {itens[computador]} e o jogador foi de {itens[jogador]}')
    else:
        print('Jogada Inválida')
elif computador == 1: #pc jogou papel
    if jogador == 0:
        print(f'O computador ganhou, pois jogou {itens[computador]} e o jogador foi de {itens[jogador]}')
    elif jogador == 1:
        print(f'Deu empate')
    elif jogador ==2:
        print(f'O jogador ganhou, pois foi de {itens[jogador]} e o pc escolheu {itens[computador]}')
    else:
        print('Jogada inválida')
elif computador == 2: #pc jogou tesoura
    if jogador == 0:
        print(f'O jogador ganhou, pois escolheu {itens[jogador]} e o pc foi de {itens[computador]}')
    elif jogador == 1:
        print(f'O computador ganhou, pois escolheu {itens[computador]} e o jogador foi de {itens[jogador]}')
    elif jogador == 2:
        print('Deu empate')
    else:
        print('Jogada inválida')
       #foi usado time (sleep) para a contagem
#varios elif aninhados
