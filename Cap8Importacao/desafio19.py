# Exercício para escolher um alune aleatório

'''import random
estudante1 = input('Primeiro aluno(a): ')
estudante2 = input('Segundo aluno(a): ')
estudante3 = input('Terceiro aluno(a): ')
lista = estudante1, estudante2, estudante3 #no exemplo da aula, a lista foi colocada entre colchete
#na verdade, toda lista tem que ficar entre colchetes.
print(f'O aluna escolhido foi {random.choice(lista)}')'''

# resoluçao da aula
import random
n1 = str(input('Primeiro Aluno (a): '))
n2 = str(input('Segundo Aluno (a): '))
n3 = str(input('Terceiro Aluno (a): '))
n4 = str(input('Quarto Aluno (a): '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

