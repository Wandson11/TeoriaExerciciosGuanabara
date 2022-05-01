dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valordia = dia * 60
valorkm = km * 0.15
print(f'Total a pagar de R$ {valordia + valorkm}')
