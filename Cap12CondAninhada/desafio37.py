#programa que leia um número inteiro qualquer e peça para escolher qual será a base de conversão.
# 1 para binário; 2 para octal; 3 para hexadecimal
#base numérica.

#está funcional, mas não identico, depois desse modelo reproduzi o da aula
'''numero = int(input('Digite um número: '))
print('Conversores:\n 1 - binário\n 2 - octal\n 3 - hexadecimal')
conversor = int(input('Digite o conversor: '))

if conversor == 1:
    print(f'O número binário de {numero} é {bin(numero)}')
elif conversor == 2:
    print(f'O número octal de {numero} é de {oct(numero)}')
else:
    print(f'O número hexadecimal de {numero} é de {hex(numero)}')'''

n1 = int(input('Digite um número: '))
print("""Opções de conversores:
 [1] - Binário
 [2] - Octal
 [3] - Hexadecimal""")
conversor = int(input('Escolha uma das opções acima: '))
if conversor == 1:
    print(f'{n1} convertido para binário é igual a {bin(n1)[2:]}')
elif conversor == 2:
    print(f'{n1} convertido para octal é igual a {oct(n1)[2:]}')
elif conversor == 3:
    print(f'{n1} convertido para hexadecimal é igual a {hex(n1)[2:]}')
else:
    print('Conversor inválido')
#detalhe importante, foi usado o fatiamento, para separar as siglas que tem no inicio de cada sequencia do conversor, mantando somente a sequencia verdadeira.