#igual ao desafio 107 mas com inclusão da moeda, por meio de uma função.



import desafio108moeda
n = float(input('Digite um preço: R$ '))
print(f'A metade de {desafio108moeda.moeda(n)} é {desafio108moeda.moeda(desafio108moeda.metade(n))}')
print(f'O dobro de {desafio108moeda.moeda(n)} é {desafio108moeda.moeda(desafio108moeda.dobro(n))}')
print(f'Aumentando 10%, temos {desafio108moeda.moeda(desafio108moeda.aumentar(n, 10))}')
print(f'Reduzindo 13%, temos {desafio108moeda.moeda(desafio108moeda.reduzir(n, 13))}')