#continuação dos dois anteriores, mas com acréscimo de um True ou False para mostrar formatação



import desafio109moeda
n = float(input('Digite o preço: R$ '))
print(f'A metade de {desafio109moeda.moeda(n)} é {desafio109moeda.metade(n, True)}')
print(f'O dobro de {desafio109moeda.moeda(n)} é {desafio109moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos {desafio109moeda.aumentar(n, 10, True)}')
print(f'Reduzindo 13%, temos {desafio109moeda.diminuir(n, 13, True)}')
