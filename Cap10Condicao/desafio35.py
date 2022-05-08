# ler o comprimento de 3 retas e diga ao usuário se elas podem ou nao formar um triangulo.
print('-=-' * 20)
print('Analisando se com as retas dá para fazer um triângulo')
print('-=-' * 20)
n1 = float(input('Digite o tamanho da primeira reta: '))
n2 = float(input('Digite o tamanho da segunda reta: '))
n3 = float(input('Digite o tamanho da terceira reta: '))

if n1 + n2 >= n3 and n2 + n3 >= n1 and n1 + n3 >= n2:
    print('Sim, é possivel fazer um triângulo com as referidas retas')
else:
    print('Não é possivel fazer um triângulo')

#resolução está muito próxima ao da aula