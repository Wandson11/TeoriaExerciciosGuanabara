#sequencia fibonacci

#não consegui fazer.
'''n1 = int(input('Quantos termos você quer mostrar? '))
c = 0
segundo = c

while c <= n1:
    print(f'{contagem}', end = ' ')
    c += 1
    contagem = contagem + c'''

# resoluçao guanabara
n1 = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end = '')
cont = 3
while cont <= n1:
    t3 = t1 + t2
    print(f'-> {t3}', end = '')
    t1 = t2
    t2 = t3
    cont += 1
print('-> Fim')


