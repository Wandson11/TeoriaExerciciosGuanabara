# Exercício de calcular a hipotenusa (na formula e pelo hypot)

# os dois primeiros eu que mexi, o terceiro é o modelo da aula.
'''from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {round(hypot(oposto, adjacente), 2)}')'''

# o modelo de baixo é feito sem a importaçao de biblioteca e de forma direta
'''oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do catego adjacente: '))
print(f'A hipotenusa vai medir {(oposto**2 + adjacente**2)**(1/2)}'''

# em aula foi feito o exemplo abaixo
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {round(hi, 3)}')
