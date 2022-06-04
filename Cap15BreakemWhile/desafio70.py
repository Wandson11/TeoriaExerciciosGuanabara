#faz um programa que role uma lista de compra,onde ao final, seja apresentado o item de maior e menor valor, e a totalização

'''print('-=-' * 10)
print('Loja Baratão')
print('-=-' * 10)
soma = caro = barato = listanome = 0


while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = int(input('Preço: '))
    soma += preco
    if preco < barato or barato == 0:
        barato = preco
        listanome = produto

    if preco >= 1000:
        caro += 1
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('Fim da compra')
print(f'O total da compra foi de R$ {soma}')
print(f'Temos {caro} Produto custando mais de mil reais')
print(f'O produto mais barato foi {listanome} custando {barato}')'''

#resolução do Guanabara
total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Qual é a mercadoria? '))
    preco = float(input('Preço: '))
    cont += 1 #isso aqui ajuda a contar o laço e fase do looping, aplicando seu resultado para verficar qual é o menor valor
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor: #os elementos a partir do or, serviram para simplificar o código.
        menor = preco
        barato = produto
    '''else:
        if menor < preco:
            menor = preco #para simplificar, foi colocado tudo isso no primeiro if do cont
            barato = produto'''
    resp = ''
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa')
print(f'O total da compra foi de R$ {total}')
print(f'Temos {totmil} custando mais de R$ 1.000')
print(f'O produto mais barato foi {barato} que custa R$ {menor}')
