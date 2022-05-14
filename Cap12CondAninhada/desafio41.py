#natação: ano de nascimento do atleta e sua categoria.
'''Até 09 anos: mirim
até 14 anos: infantil
até 19 anos: junior
até 20 anos: sênior
acima de 20: master'''

#ao inves de fixar a data de 2022, importei o datetime
from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade <= 9:
    print(f'Sua idade é de {idade} anos e sua categoria é mirim')
elif 14 >= idade > 9: #aqui foi apresentado que, nao precisa colocar mais um segmento, pode ser resumudi assim: idade <= 14
    print(f'Sua idade é de {idade} anos e sua categoria é infantil')
elif 19 >= idade > 14: # idade <= 19
    print(f'Sua idade é de {idade} anos e a sua categoria é junior')
elif 25 >= idade > 19: # idade <=25
    print(f'Sua idade é de {idade} anos e a sua categoria é sênior')
elif idade > 25: # idade > 25
    print(f'Sua idade é de {idade} anos e a sua categoria é master')