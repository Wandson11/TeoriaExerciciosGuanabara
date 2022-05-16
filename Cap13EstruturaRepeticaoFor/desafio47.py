#mostrar na tela todos os números pares que estao no intervalo de 0 a 50

for c in range(2, 51, 2):
    print(f'{c}', end= ' ')
print('fim')

#Abaixo a resolução do guanabara
'''
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end= ' ')
'''
#tem um problema nessa resoluçao, ele faz dois lanços para tirar um número, enquanto que na minha resoluçao (a primeira), que tbem foi feita em aula, só usa uma.
# isso é bom, pois tira carga do processador, onde a primeira opçao fez o mesmo trabalho, com a metade do trabalho.

#essa resposta abaixo, tirei dos comentários da aula.
for c in range(1, 26):
    print(c*2, end = ' ')
