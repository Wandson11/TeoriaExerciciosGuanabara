# exercício para apurar o valor a ser pago de um aluguel de carro, com valor diário a ser pago e por km percorrido.

dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valordia = dia * 60
valorkm = km * 0.15
print(f'Total a pagar de R$ {valordia + valorkm}')
