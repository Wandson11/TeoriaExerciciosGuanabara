# Exercícios para calcular o seno, coseno e tangente, usando math)
# no caso, inicialmente tava dando erro, mas pesquisando vi que necessitava da conversao de graus/radianos
# esse primeiro modelo foi o que eu fiz, esta funcional
'''from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {ang} tem o SENO de {sin(radians(ang))}')
print(f'O ângulo de {ang} tem o COSSENO de {cos(radians(ang))}')
print(f'O ângulo de {ang} tem um TANGENTE de {tan(radians(ang))}')'''

import math
angu = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angu))
print(f'O ângulo digitado foi de {angu} e o seu Seno é de {round(seno, 2)}')
cose = math.cos(math.radians(angu))
print(f'O ângulo digitado foi de {angu} e o seu Coseno é de {round(cose, 2)}')
tang = math.tan(math.radians(angu))
print(f'O ângulo digitado foi de {angu} e o seu Tangente é de {round(tang, 2)}')



