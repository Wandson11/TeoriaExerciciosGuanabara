#Aula de condecional

'''nome = str(input('Qual é o seu nome: ')).strip()
if nome == 'Wandson':
    print('Que nome bonito você tem')
else:
    print('Que nome sem graça')
print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2)/2
print(f'Sua média foi de {media}')
if media >= 6:
    print(f'Sua média geral foi boa!')
else:
    print(f'Sua média geral foi baixa!')
'''print('Parabens' if media >= 6 else 'Estude mais')'''
#quando for simples, atençao com as aspas, a formula fica de fora dela.
