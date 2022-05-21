#programa que ler o peso de 5 pessoas, e fala quem pesa mais e menos
'''lista = 0
for c in range(1, 6):
    peso = float(input('Qual é o seu peso? '))
lista = max(peso)
print(f'O mais pesado é {lista}')'''
#nao consegui resolver.

'''maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'O peso da {c}º pessoa é de: '))
    if c == 1:
            maior = peso
            menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso registrado foi de {maior}kg')
print((f'O menor peso registrado foi de {menor}kg'))'''


#exemplo retirado dos comnetários
lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista



