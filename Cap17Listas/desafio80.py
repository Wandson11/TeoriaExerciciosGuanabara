#digitar 5 valores númericos e cadastrar em uma lista.
#inserir cada valor em ordem crescente em sua posiçao correta.
# sem ajuda do sort()

#está funcional mas ficou gigante
'''lista = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0:
        lista.append(numero)
        print('Adicionado no final da lista')
    if c == 1:
        if numero < lista[0]:
            lista.insert(0, numero)
            print(f'Adicionado na posição 0 da lista')
        else:
            lista.insert(1, numero)
            print(f'Adicionaldo na posição 1 da lista')
    if c == 2:
        if numero < lista[0] and numero < lista[1]:
            lista.insert(0, numero)
            print(f'Adicionaldo na posição 0 da lista')
        elif numero > lista[0] and numero > lista[1]:
            lista.insert(2, numero)
            print(f'Adicionaldo na posição 2 da lista')
        elif numero > lista[0] and numero < lista[1]:
            lista.insert(1, numero)
            print(f'Adicionaldo na posição 1 da lista')
    if c == 3:
        if numero > lista[2]:
            lista.insert(3, numero)
            print(f'Adicionaldo na posição 3 da lista')
        elif numero < lista[0]:
            lista.insert(0, numero)
        elif numero > lista[0] and numero < lista[1]:
            lista.insert(1, numero)
            print(f'Adicionaldo na posição 1 da lista')
        elif numero > lista[1] and numero < lista[2]:
            lista.insert(2, numero)
            print(f'Adicionaldo na posição 2 da lista')
    if c == 4:
        if numero > lista[3]:
            lista.insert(4, numero)
            print(f'Adicionaldo na posição 4 da lista')
        elif numero < lista[0]:
            lista.insert(0, numero)
            print(f'Adicionaldo na posição 0 da lista')
        elif numero > lista[0] and numero < lista[1]:
            lista.insert(1, numero)
            print(f'Adicionaldo na posição 1 da lista')
        elif numero > lista[1] and numero < lista[2]:
            lista.insert(2, numero)
            print(f'Adicionaldo na posição 2 da lista')
        elif numero > lista[2] and numero < lista[3]:
            lista.insert(3, numero)
            print(f'Adicionaldo na posição 3 da lista')
print(lista)'''

#resoluçao na caixa de comentários.
'''lis = [ ]
for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    if c == 1 or n >= lis[-1]:
        lis.append(n)
    elif n <= lis[0]:
        lis.insert(0, n)
    elif lis[0] <= n <= lis[1]:
        lis.insert(1, n)
    elif lis[1] <= n <= lis[2]:
        lis.insert(2, n)
    elif lis[2] <= n <= lis[3]:
        lis.insert(3, n)
print(lis)'''

#Resoluçao do guanabara
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicional ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]: #essa parte eu nao entendi : lista[pos]
                lista.insert(pos, n)
                print(f'Adicionado na posiçao {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')