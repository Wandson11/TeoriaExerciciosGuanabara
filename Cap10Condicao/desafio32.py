# escreve um ano e mostre se ele é bissexto

'''bissexto = int(input('É um ano bissexto? '))
if (bissexto % 4) == 0:
    print('É um ano bissexto')
else:
    print('Nao é um ano bissexto')'''

#exercicio resolvido, nota-se a utilizaçao de 'and' e 'or'
from datetime import date
bissexto = int(input('É um ano bissexto? Coloque 0 para analisar o ano atual: '))
if bissexto == 0: #isso daqui é para pegar a data referência no dia que tiver fazendo.
    bissexto = date.today().year
if bissexto % 4 == 0 and bissexto % 100 != 0 or bissexto % 400 == 0:
    print(f'O ano de {bissexto} é bissexto')
else:
    print(f'O ano {bissexto}, NÃO é bissexto')
