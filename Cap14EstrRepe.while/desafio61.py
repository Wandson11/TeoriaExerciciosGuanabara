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

while 