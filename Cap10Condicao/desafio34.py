#programa que pergunte o salário de um func. e cálcule o valor do seu aumento.

#está funcional
'''salario = float(input('Qual é o seu salário? ')) # aqui tem um problema, se na resposta, nao colocar o ponto (1.500), o programa vai entender como > 1250
if salario > 1250:
    print(f'Pela regra, seu salário será reaustado em 10%, que significa um aumento de R$ {salario * 0.10}, totalizando R$ {salario * 0.10 + salario}')
else:
    print(f'Seu salário será reajustado em 15%, referente a um aumento de R$ {salario * 0.15}, totalizando assim, um novo vencimento de {salario * 0.15 + salario}')'''

salario = float(input('Valor do salário: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R$ {salario} passa a ganhar R$ {novo}')