#faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

#esse eu nao consegui fazer, pegue os dois exemplos na net.
'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'O maior número é {maior}')'''

'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
lista = [n1, n2, n3]
maior = max(lista)
minimo = min(lista)
print(f'O maior número é {maior}')
print(f'O menor número é {minimo}')'''

#resoluçao da aula do guanabara
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
#verificando menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor digitado foi {menor}')
#verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado foi {maior}')


