#calcular o fatorial

n1 = int(input('Digite um número para cálcular o fatorial: '))
fatorial = n1
f = 1 # isso aqui nao tinha colocado.
while fatorial > 0: # aqui tentei conciliar com n1 ficando while fatorial < n1, mas no caso, era mais simples
    print(f'{fatorial}', end='')
    print(' x ' if fatorial > 1 else ' =', end= '')# aqui, outro detalhe, condicional de formatação
    f *= fatorial
    fatorial -= 1 # aqui, no acumulador, detalhe importante, se ao invés de inserir o += e acrescentar -=, a contagem fica inversa.
print(f'{f}')# aqui, o resultando ficou fora do laço e entrou no print geral depos do sinal de igual


#fatorial com impor
'''from math import factorial
n1 =int(input('Digite um número para calcular a fatorial: '))
print(f'{factorial(n1)}')'''

#na aula, Guanabara apresenta uma resolução igual a de cima.

#foi pedido para fazer uma tarefa com esse temática mas por meio do for: 
n1 = int(input('Digite um número fatorial: '))
contagem = 0
fator = 1
for c in range(n1, 0, -1):
    contagem += 1
    print(f'{c}', end = ' ')
    print(' x ' if c > 1 else ' =', end= ' ')
    fator *= c
print(f'{fator}', end= ' ')
#no caso, com a contagem é decrescente, começou por n1, posteriormente, foi usado a contagem += 1, para incluir todos os números da fatorial, ainda foi usado o "fator" com multiplicação.
# outro ponto, foi o segundo print para inserir o x e o =, na hora correta, reflexo da resolução da aula.
