#faz um programa que role uma lista de compra,onde ao final, seja apresentado o item de maior e menor valor, e a totalização

print('-=-' * 10)
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
print(f'O produto mais barato foi {listanome} custando {barato}')