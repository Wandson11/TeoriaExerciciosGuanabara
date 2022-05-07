#crie um programa que leia um número inteiro que mostre na tela se ela é par ou impar

jogo = int(input('Digite um número: '))
if (jogo % 2 ) == 0:
    print(f'Esse número é par')
else:
    print(f'Esse número é impar')