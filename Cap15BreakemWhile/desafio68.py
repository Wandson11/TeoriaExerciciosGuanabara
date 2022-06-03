#jogar par ou ímpar com o pc
#jogo será interrompido quando o jogador perder
#mostrando o total de vitorias consecutivas da pessoa


'''from random import randint
computador = randint(0, 10)
soma = 0
conta = 0

while True:
    valor = int(input('Digite um valor: '))
    jogador = str(input('Par ou ímpar: [P/I] '))
    print(computador)
    conta = computador + valor
    if conta % 2 == 0 and jogador == 'i':
        break
    elif conta % 2 == 1 and jogador == 'p':
        break
    print(f'O computador jogou {computador} e você jogou {valor}, totalizando {conta} = {jogador}')
    soma += 1
    computador = 0
print(f'Você perdeu, deu {conta}, total de acertos {soma}')'''

#resolução do guanabara
from random import randint
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total =computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar: [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end = ' ')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print(f'Game Over, você venceu {v} vez(es)')
