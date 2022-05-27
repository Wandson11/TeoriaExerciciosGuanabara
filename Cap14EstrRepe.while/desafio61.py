#progressão aritmética com while

#fiz o modelo abaixo para relembar a forma com for
'''n1 = int(input('Primeiro termo:'))
n2 = int(input('Qual a razão: '))

enesima = n1 + (10 - 1) * n2
soma = 0
for c in range(n1, enesima + n2, n2):
    print(c, end = '')
    print('->' if c < enesima else '-> Fim', end = ' ')
    soma += 1'''

n1 = int(input('Digite o termo inicial: '))
n2 = int(input('Digite a razão: '))

#resoluçao vista nos comentários.
'''n1 = int(input('Digite o termo inicial: '))
n2 = int(input('Digite a razão: '))
enesimo = n1 + (10-1) * n2
c = 10 # nao entendi isso aqui
while c > 0:
    print(f'{n1}')
    n1 = n1 + n2
    c = c -1
print('fechando')'''

#nao precisa da enésima
#resoluçao do guanabara.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}')
    termo += razao
    cont += 1
