# calcular o imc
'''
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
acima de 40: obesidade mórbida
'''
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
print(f'Seu imc é de {round(imc, 2)}')
if imc < 18.5:
    print(f'Seu IMC de {round(imc, 2)} está categorizado como abaixo do peso')
elif imc <= 25:
    print(f'Seu IMC de {round(imc, 2)} está categorizado como peso ideal')
elif imc <= 30:
    print(f'Seu IMC de {round(imc, 2)} está categorizado como sobrepeso')
elif imc <=40:
    print(f'Seu IMC de {round(imc, 2)} está categorizado como obeso')
elif imc > 40:
    print(f'Seu IMC de {round(imc, 2)} está categorizado como obesidade mórbida.')
