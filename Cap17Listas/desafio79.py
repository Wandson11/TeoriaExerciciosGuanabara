# programa que o usuário digite vários valores, sem restriçoes, cadastrando em uma lista.
# caso já exista, ele nao será adicionado.
# no final, serao exibidos todos os valores unicos em forma crescente.

#nao consegui fazer, pois nao foram afastados os valores duplicados.
'''lista = []

while True:
    teste = lista.append(int(input('Digite um valor: ')))
    if teste != lista: #if teste in lista
        print('Valor adicionado')
    else:
        print('Duplicado')
    pergunta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if pergunta == 'N':
        break
lista.sort()
print(lista)'''

#resoluçao vista no caixa de comentários.
#usou remove mas nao o append.
'''lista = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n in lista:
        print('ESSE NÚMERO JÁ CONSTA NA LISTA.')
        lista.remove(n)

    lista += [n]

    flag = str(input('Continuar? (S/N): ')).strip().lower()[0]
    if flag == 'n':
        print(f'\nOs números digitados foram {sorted(lista)}')
        break'''

#resolução guanabara
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
números.sort()
print(f'Você digitou os seguintes valores {números}')