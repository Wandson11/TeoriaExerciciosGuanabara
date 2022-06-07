#aula 16 - Tupla.
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#len tbem ignora o último valor
for cont in range(0, len(lanche)): #com o cont,mostra a posição.
for c in lanche:
    print(f'Comi muito {c}')
print('TÔ cheio')

for pos, comida in enumerate(lanche):
    print(f'Comi muito {comida} na posição {pos}')
    #apagar tupla del(lanche)