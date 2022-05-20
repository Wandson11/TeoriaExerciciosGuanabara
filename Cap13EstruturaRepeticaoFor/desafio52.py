# programa que leia um número inteiro e diga se ele é ou não número primo

n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1 +1):
    if n1 % c ==0:
        print('\033[33m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print(c, end= ' ')
print(f'\n\033[mO número {n1} é divisível {tot} vez(es)')
if tot ==2 :
    print('É um número primo')
else:
    print('Nao é um número primo')