#programa que aponte se, a erro ou nao na aplicaçao dos parenteses em uma fórmula matemática.

#pelos meus testes, deu certo.
'''lista = ['()', '(())', '((()))', '(((())))']
calculo = str(input('Digite a sua expressão: '))
if calculo in lista:
    print('Essa expressao está certa')
else:
    print('Essa expressao está errada')'''

# resolução dos comentários.
'''calculo = str(input('Digite uma expressão: '))

if calculo.count('(') == calculo.count(')'):
    print('Essa expressão é válida.')
else:
    print('Expressão inválida')'''

#Guanabara

expr = str(input('Digite uma expressão: '))
pilha = []
for sim in expr:
    if sim == '(':
        pilha.append(sim)
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop() #vai excluir o último
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao é válida')
else:
    print('Expressao inválida')
