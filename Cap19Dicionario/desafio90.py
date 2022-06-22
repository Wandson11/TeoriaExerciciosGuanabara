#programa que leia o nome e a média de um aluno
#guardando a situaçao em um dicionário (aprovado/reprovado)


'''aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(f'O nome do aluno é {aluno["Nome"]}')
print(f'Média é igual a {aluno["Média"]}')
print(f'Com essa média o aluno foi {aluno["Situação"]}')'''

#Resolução Guanabara
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}'))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] <7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items(): #k de key, v de values.
    print(f'{k} é igual a {v}')

