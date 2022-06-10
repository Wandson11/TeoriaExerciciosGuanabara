#lista de preço,

#dessa vez, não consegui fazer sozinho, fiz de acordo com uma ideia nos comentários do video
#que falava na utilização do type para filtrar str e float, seprando individualmente da tuplas

'''lista = ('Banana', 09.7, 'Arroz', 22.5, 'Feijão', 09.5, 'Caderno', 45.0)

print('-=-' * 10)
print(f'{"Lista de Preço" : ^27}')
print('-=-' * 10)

for c in lista:
    if type(c) == str:
        print(f'{c : <7}', end = '')
    if type(c) == float:
        print(f'{".." * 10} {"R$" : >2}', end = ' ')
        print(f'{ c : >1}')'''

listagem = ('Lapis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9)

print('-=-' * 20)
print(f'{"lista de preço":^40}')
print('-=-' * 20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0: #aqui usou a premisa que, todo produto se encontra como sendo par.
        print(f'{listagem[pos]:.<30}', end = '') #se colocar o ponto entre ":" e "<", o mesmo vai criar uma linha.
    else:
        print(f'R${listagem[pos]:>7.2f}')# o .2f, aponta pela qtde da casa decimal
print('-=-' * 20)

