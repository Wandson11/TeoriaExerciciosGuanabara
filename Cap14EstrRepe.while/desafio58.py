#upgrade do desafio 28, pc vai pensar em um número de 0 a 10,
# jogador vai tentar adivinhar até acertar.
# mostrando quantos palpites foram necessários.

'''from random import randint
pc = randint(0, 10)
tentativas = 0
adivinha = int(input('Qual é o número da maquina? '))
while adivinha != pc:
    adivinha = int(input('Errou, tente novamente: '))
    tentativas += 1
print(f'{pc}') #coloquei isso, para verificar se os valores estão batendo.
print(f'Acertou, o número escolhido foi {adivinha}, e foram necessárias {tentativas+1} tentativas')'''

#modelo do guanabara
from random import randint
computador = randint(0, 10)
print('Sou seu computador e pensei em um número de 0 a 10')
print('Você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite o número: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else: #aqui, foi um enxerto, para dar dica.
        if jogador < computador:
            print('O número é maior')
        elif jogador > computador:
            print('O número é menor')
print(f'Voce acertou na {palpites} tentativa')
