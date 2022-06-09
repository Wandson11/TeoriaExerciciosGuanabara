#tabela brasileiro serie b

#minha solução
'''tabela = ('Cruzeiro', 'Bahia', 'Vasco da Gama', 'Sport', 'Grêmio', 'Operário', 'Novo Horizontino',
          'Brusque', 'Criciúma', 'Tombense', 'CSA', 'Sampaio Correa', 'Ponte Preta',
          'Londrina', 'Náutico', 'Chapecoense', 'CRB', 'Ituano', 'Vila Nova', 'Guarani')

print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('-=-' * 20)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('-=-' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=-' * 20)
print(f'O Chapecoense está na {tabela.index("Chapecoense")}ª posição')'''

#guanabara

times = ('Cruzeiro', 'Bahia', 'Vasco da Gama', 'Sport', 'Grêmio', 'Operário', 'Novo Horizontino',
          'Brusque', 'Criciúma', 'Tombense', 'CSA', 'Sampaio Correa', 'Ponte Preta',
          'Londrina', 'Náutico', 'Chapecoense', 'CRB', 'Ituano', 'Vila Nova', 'Guarani')

print('-=' * 15)
print(f'Lista de times do brasileirão {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição')
