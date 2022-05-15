# laços de repetição
'''i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for abacaxi in range(i, f+1, p):
    print(abacaxi)
print('Fim')'''

s = 0 # está vinculado ao somatório de baixo.
for c in range(0,4):
    n = int(input('Digite um número: '))
    s += n # isso aqui, é a versao do python para o somatório, que representa o seguinte s = s + n
print(f'O somatório de todos os valores digitado foi de {s}')
