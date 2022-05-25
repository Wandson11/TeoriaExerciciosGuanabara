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