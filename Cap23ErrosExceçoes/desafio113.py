#reutilizar o desafio 104, com input que pede número real e inteiro
#utilizando os elementos apredendidos na aula 23


def leiaint(msg):
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('Voce digitou algo inválido')
            continue#joga pro laço de novo
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            m = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('Você digitou um valor inválido, escolha apenas números reais')
            continue
        except KeyboardInterrupt:
            print('O usuário suspendeu o preenchimento')
            return 0
        else:
            return m


n= leiaint('Digite um número inteiro: ')
m = leiafloat('Digite um número real: ')
print(f'Voce acabou de digitar o número inteiro {n} e o real de {m}')