#aprovar um empréstimo bancário para a compra de uma casa, pergunta o valor da casa, o salário do comprador e o tempo de pgto.
#calcular o valor da prestação, não excedendo 30% do salário, ou então, o empréstimo será negado.

#fiz por meses, cálculo está funcional
casa = float(input('Qual é o valor do imóvel? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
prestacao = int(input('Em quantos meses deseja pagar? ')) #* 12conforme acima, fiz em meses mas se for colocar em ano e só inserir o * 12 ao final
valorpossivel = casa / prestacao * 1000
limite = salario * 0.30 * 1000

if limite >= valorpossivel:
    print(f'Crédito aprovado, a prestação máxima é de {valorpossivel} e voce consegue pagar {round(limite, 2)}.')
else:
    print(f'Empréstimo reprovado, pois a parcela mínima é de {valorpossivel} e voce só consegue comprometer {round(limite, 2)}')

# meu modelo ficou muito parecido com o do exércicio, assim, não o reproduzi a resolução da aula.




