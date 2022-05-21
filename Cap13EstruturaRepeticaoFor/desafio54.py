#ler os anos, no final, apontar quantas não atingiram a maioridade.
from datetime import date
hj = date.today().year
maioridade = 0
menor = 0
for c in range(1, 8):
    data = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = hj - data
    if idade >= 18:
        maioridade += 1
    else:
        menor += 1
print(f'Ao todo, tem-se {maioridade} pessoa (s), maior(es) de idade')
print(f'E também, tem-se {menor} pessoa (s), menor(es) de idade')

#minha resoluçao ficou igual do Guanabara.
