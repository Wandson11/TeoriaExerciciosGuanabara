#jogar par ou ímpar com o pc
#jogo será interrompido quando o jogador perder
#mostrando o total de vitorias consecutivas da pessoa


from random import randint
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
print(f'Você perdeu, deu {conta}, total de acertos {soma}')
