#nome e peso das pessoas, colocando essas informações em uma lista.
#qtas foram cadastradas
#lista com as pessoas mais pesadas
#lista com as pessoas mais leves

'''lista = []
novalista = []
maispesado = leve = 0
nomedoobeso = ''
nomedoleve = ''
while True:
    lista.append(str(input('Digite o seu nome: ')))
    lista.append(int(input('Digite o seu peso: ')))
    novalista.append(lista[:])
    lista.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar in 'N':
        break
print(novalista)
print(f'Ao todo, foram cadastradas {len(novalista)}') #1
for peso in novalista:
    if peso[1] == maispesado:
        maispesado = peso[1]
        nomedoobeso = peso[0]
    else:
        if peso[1] > maispesado:
            maispesado = peso[1]
            nomedoobeso = peso[0]
print(f'O maior peso registrado foi de {maispesado}kg, pertencente a {nomedoobeso}')
for levinho in novalista:
    if peso[1] == leve:
        leve = peso[1]
        nomedoleve = peso[0]
    else:
        if leve < peso[1]:
            leve = peso[1]
            nomedoleve = peso[0]
        else:
            leve = peso[1]
            nomedoleve = peso[0]
print(f'O menor peso registrado foi de {leve}kg, pertencente a {nomedoleve}')'''

#Guanabara
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Digite o seu nome: ')))
    temp.append(int(input('Digite a idade: ')))
    if len(princ) == 0: #usou o len para apontar que, caso estivesse no laço zero, o maior e menor seriam o mesmo número
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break

print(f'Ao todo, foram cadastrados {len(princ)} pessoas')
print(f'O maior peso foi de {maior} kg. Peso de ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} ', end=' ')
print()
print(f'O menor peso foi de {menor} kg. Peso de', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end=' ')
print()
