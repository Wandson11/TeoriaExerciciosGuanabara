# Exercício é o de fazer uma lista randomizada para a uma apresentaçao
# está funcional
'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
print(f'A ordem da apresentação será: {random.sample(lista, 4)}')'''
# observaçao importante, pelo "sample", dá para limitar a quantidade de gente, por exemplo se tiveram 10, dá para limitar em "k", a quantidade que vao apresentar.

#usado na aula
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) # AQUI FOI DIFERENTE, COLOCOU A FORMULA FORA DE QUAQLUER VARIAVEL, PARA JÁ MISTURAR A LISTA
print(f'A ordem da apresentaçao será {lista}')