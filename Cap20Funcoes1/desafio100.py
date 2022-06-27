#programa tem que uma lista chamada números
#ter duas funções sorteia() e somapar()
#a primeira função vai sortear e colocar 5 valores dentro da lista.
#a segunda função, vai mostrar a soma apenas dos valores pares.


'''from time import sleep
from random import randint
números = []
def sorteia():
    print(f'Os números sorteados são: ', end=' ')
    for c in range(1, 6):
        #números.append(randint(1, 10))
        sorteio = randint(1, 10)
        números.append(sorteio)
        print(sorteio, end=' ')
    print()
sorteia()
def somapar():
    cont = 0
    for c in números:
        if c % 2 == 0:
            cont += c
    print(f'Somando os valores pares da lista {números}, temos {cont}')

somapar()'''

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('Pronto')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 ==0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos {soma}')

números=list()
sorteia(números)
somapar(números)