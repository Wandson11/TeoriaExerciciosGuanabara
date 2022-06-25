#funçao chamada contador(), que receba 3 parametros, inicio, fim e passo
#o programa tem que rodar 3 contagens:
#a) de 1 a 10, de um em um
#b) de 10 a 0, de 2 em 2.
#c) uma contagem personalizada.

'''from time import sleep
def contador():
    print('~' * 15)
    for c in range(1, 11, 1):
        print(c, end=' ')
        sleep(0.1)
    print()
    for v in range(10, -1, -2):
        print(v, end=' ')
        sleep(0.1)
    print()
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio > fim and passo < 0:
        for cont in range(inicio, fim, passo):
            print(cont, end=' ')
            sleep(0.1)
        print()
    elif inicio > fim and passo > 0:
        for cont in range(inicio, fim, passo*-1):
            print(cont, end=' ')
            sleep(0.1)
        print()
    elif passo == 0 and inicio < fim:
        for c in range(inicio, fim, 1):
            print(c, end=' ')
            sleep(0.1)
        print()
    elif passo == 0 and inicio > fim:
        for c in range(inicio, fim, -1):
            print(c, end=' ')
            sleep(0.1)
        print()
contador()'''

#Guanabara
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('Fim')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

