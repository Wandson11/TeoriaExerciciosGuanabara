#digitar 5 números e guarde-os em uma lista
#apresente todos os números digitados, o maior e o menor, e a sua posiçao na lista

'''lista = []
for c in range(0,5): #aqui foi formada a lista com o seus elementos.
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

#for colocacao, valor in enumerate(lista):
#    print(f'O valor {valor} apareceu na colocaçao {colocacao}')


print(f'Os valores digitados foram {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi {min(lista)} na posiçao {lista.index(min(lista))}')'''

#Guanabara
listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} na posiçao', end=' ')
for i, v in enumerate(listanum): #indice, valor.
    if v == mai:
        print(f'{i}...', end='')
print()#se deixar esse print sem nada, nao acumular tudo na mesma linha por causa do end
print(f'O menor valor digitado foi {men} na posição', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')