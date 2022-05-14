# calcular o valor a ser pago por um produto, considerando o preço no varejo e sua forma de pagamento.
'''
a vista dinheiro/cheque: 10% desconto
a vista cartao: 5%
em até 2x no cartão: preço normal
3 x ou mais no cartão, juros de 20%
'''

'''valor = int(input('Preço da mercadoria: '))
print('[1]a vista em dinheiro/cheque\n[2]a vista com cartão\n[3]Cartão em duas parcelas\n[4]Cartão em 3 parcelas ou mais')
pgto = int(input('Forma de pagamento: '))

if pgto == 1:
    desconto = valor * 0.1
    print(f'O valor a vista, com desconto de 10% de R$ {desconto}, perfazendo assim, o valor de R$ {valor - desconto}')
elif pgto == 2:
    desconto = valor * 0.05
    print(f'O valor a vista, com pagamento no cartão, tem desconto de 5% no valor de {desconto}, perfazendo assim em {valor - desconto}')
elif pgto == 3:
    print(f'Parcelado em 2 vezes de R$ {valor/2}')
elif pgto == 4:
    parcelado = int(input('Em quantas vezes? '))
    if parcelado == 4 or 5 or 6:
        juros = valor * 0.2 + valor
        parcela = juros / parcelado
        print(f'No cartão, em {parcelado} vezes com juros de 20%, cada parcela custará R$ {parcela}')
else:
    print('Pagamento inválido')

# minha resolução ficou muito próxima ao do guanabará, diferença ficou em fazer novas variaveis para os cálculos, enquanto eu coloquei dentro das chaves {} os cálculos matemáticos.'''

#reproduzindo o da aula
valor = int(input('Qual é o valor? '))
print('[1]a vista em dinheiro/cheque\n[2]a vista com cartão\n[3]Cartão em duas parcelas\n[4]Cartão em 3 parcelas ou mais')
pagamento = int(input('Forma de pagamento: '))

if pagamento == 1:
    total = valor - (valor * 0.1)
elif pagamento == 2:
    total = valor - (valor * 0.05)
elif pagamento == 3:
    total = valor
    parcela = total / 2
    print(f'Sem desconto, mas dividido em 2 parcelas de {parcela}')
elif pagamento == 4:
    total = valor + (valor * 0.2)
    totalpar = int(input('Em quantas vezes? '))
    parcela = total / totalpar
    print(f'Sua compra será parcelado em {totalpar}x de R$ {parcela} ')
else:
    total = 0
    print('Opção inválida de pagamento, tente novamente')
#nesse ponto, cabe um comentário, pois na aula foi usado somente um print para as duas possibilidades
print(f'O valor da mercadoria ficou em R$ {total}')
