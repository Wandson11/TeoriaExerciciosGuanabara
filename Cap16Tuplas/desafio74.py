#gerar 5 números aleatórios e inserir em uma tupla.
#depois, mostrar quais são esses números, o menor e o maior.

from random import randint
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#testei pelo Sample, mas não dá, pq o mesmo não repete o número, e no modelo do exercício, isso acontece

'''contador = inserir = 0
for c in range (1, 5):
    aleatório = randint(1, 10)
    inserir += aleatório
    tupla = (aleatório, )
    contador += 1

print(f'deu errado {tupla}')'''
'''c = tupla = 0
while c <= 5:
    escolha = randint(1,10)
    tupla += (escolha,)
    c+=1
print(tupla)'''

#resolução guanabara

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),)
print('Os valores sorteados foram: ')

for c in numeros:
    print(f'{c}', end= ' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')