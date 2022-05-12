# escreva um programa que leia 2 números inteiros e compare-os:
# o primeiro valor é maior; o segundo valor é maior; nao existe valor maior, os dois são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
if n1 > n2:
    print(f'O primeiro valor é maior, pois {n1} > {n2}')
elif n2 > n1:
    print((f'O segundo valor é maior, pois {n2} > {n1}'))
else:
    print(f'Os \033[1;31;45mvalores\033[m são iguais, {n1} = {n2}')