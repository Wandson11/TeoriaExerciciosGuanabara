#programa que leia o nome, sexo e idade de várias pessoas,
#guardando os dados em um dicionário e todos em uma lista
#para mostrar:
#a)qtas pessoas cadastradas;
#b) uma lista com mulheres;
#c) uma lista com idade acima da média

'''dados = dict()
arquivo = list()
idade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
    dados['idade'] = int(input('Idade: '))
    idade += dados['idade']
    arquivo.append(dados.copy())
    continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print(arquivo)
print('-=' * 15)
print(f'Foram cadastradas {len(arquivo)} pessoas')
print('-=' * 15)
média = idade/len(arquivo)
print(f'A média de idade foi de {média}')
print('-=' * 15)
print(f'Alista de mulheres no grupo sao: ', end=' ')
for c in range(0, len(arquivo)):
    if arquivo[c]['sexo'] in 'Ff':
        print({arquivo[c]["nome"]})
print()
print('-=' * 15)
print(f'Lista de pessoas com idade acima da média:\n')
for c in range(0, len(arquivo)):
    if arquivo[c]['idade'] >= média:
        print(f'{arquivo[c]}')'''

#Guanabara
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True: #validação
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print(f'Ao todo  temos {len(galera)} pessoas cadastradas')
média = soma/ len(galera)
print(f'A média de idade é d e {média:5.2f} anos')#5 casa e 2 decimais.
print('As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas que estao com idade acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('Encerrado')