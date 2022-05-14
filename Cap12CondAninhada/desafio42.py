#refazer o exercício 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
'''
equilatero: todos lados iguais
escaleno: todos diferentes
isósceles: dois iguais
'''
n1 = float(input('Digite a primeira reta: '))
n2 = float(input('Digite a segunda reta: '))
n3 = float(input('Digite a terceira reta: '))
if n1 + n2 >= n3 and n2 + n3 >= n1 and n1 + n3 >= n2:
    print(f'Sim, é um triângulo!')
    if n1 != n2 != n3 != n1:#aqui eu errei pela diferença de n3 e n1, no final foi incluso '!= n1'S
        print('Todos os lados sao diferentes, portanto, escaleno')
    elif n1 == n2 == n3:
        print('Todos os lados são iguais, portanto, equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Tem dois lados iguais, portanto, é um isósceles.')

else:
    print('Pelo tamanho das retas não dá para fazer um triângulo')
print('-=-' * 20)
