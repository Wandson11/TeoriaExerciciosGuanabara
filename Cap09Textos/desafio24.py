# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome de 'santo'

local = str(input('Digite o nome de uma cidade: '))
separando = local.split()
primeironome = separando[0]
print('Santo' in primeironome)
