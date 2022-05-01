vencimentos = float(input('Qual é o salario do funcionário? '))
reajuste = vencimentos * 0.15
print(f'Um funcionário que ganhava R$ {vencimentos}, com 15% de aumento, passa a receber R$ {round(vencimentos + reajuste, 2)}')
