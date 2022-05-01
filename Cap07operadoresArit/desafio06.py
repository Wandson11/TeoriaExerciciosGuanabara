# exercicio para calcular o dobro, triplo e a raiz quadrada de um numero digitado no input
# no caso, nao fiz novas variaveis para cada operaçao, coloquei as formulas dentro da chave
# é dito em aula que se o resultado dessas variaveis com fórmulas matemáticas forem aproveitadas futuramente, o melhor é fazer com variavel, ou seja,
# uma variavel para cada operação.
# usei round(), para delimitar as casas decimais. O exemplo da aula é diferente {:.2f}
# \n para quebrar linhas

n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n*2} \n O triplo de {n} é {n*3} \nE a raiz quadrada de {n} é igual a {round(n**(1/2),2)}')



