#programa que ler o nome e duas notas, e coloque em uma lista. (3 níveis de listas)
#média

'''listamaior = []
listamedia = []
listamenor = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    listamedia.append(nome)
    nota1 = int(input('Digite a 1ª nota: '))
    listamenor.append(nota1)
    nota2 = int(input('Digite a 2ª nota: '))
    listamenor.append(nota2)
    listamedia.append(listamenor[:])
    listamaior.append(listamedia[:])
    listamenor.clear()
    listamedia.clear()
    continuar = str(input('Desejar continuar? ')).upper()
    if continuar != 'S':
        break
print(listamaior)
print('No Nome Média')
for ind, valor in enumerate(listamaior):
    print(f'{ind} {valor[0]} {(valor[1][0] + valor[1][1]) / 2}')

while True:
    resumo = int(input('Mostrar nota de qual aluno? de acordo com o índice. 999 interrompe '))
    if resumo == 999:
        break
    print(f'Notas de {listamaior[resumo][0]} sao {listamaior[resumo][1]}')'''

#Guanabara
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-=' * 26)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-=' * 20)
    opc = int(input('Mostrar de qual aluno: (999 interrompe) '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')


