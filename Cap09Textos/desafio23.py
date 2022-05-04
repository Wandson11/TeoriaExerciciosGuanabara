#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

n = str(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {n[3:]}')
print(f'Dezena: {n[2:3]}')
print(f'Centena: {n[1:2]}')
print(f'Milhar: {n[:1]}')

