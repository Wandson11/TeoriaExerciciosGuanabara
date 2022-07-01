#módulo moeda que tenha funções: aumentar(); diminuir(); dobro() e metade()

import desafio107moeda
p = int(input('Digite o preço: R$ '))
print(f'A metade de {p} é {desafio107moeda.metade(p)}')
print(f'O dobro de {p} é {desafio107moeda.dobro(p)}')
print(f'Aumentando 10%, temos {desafio107moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {desafio107moeda.reduzir(p, 13)}')