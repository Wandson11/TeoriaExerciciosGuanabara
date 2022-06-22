#programa que leia nome, data de nascimento e carteira de trabalho
#se carteira for zero, termina ali mesmo

'''from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
anonascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - anonascimento
cadastro['carteira'] = int(input('Possui carteira de trabalho? [0 não tem]: '))
if cadastro['carteira'] != 0:
    cadastro['contratação'] = int(input('Ano da contratação: '))
    cadastro['salário'] = int(input('Salário: '))
    aposentar = cadastro['contratação'] - anonascimento
    cadastro['aposentadoria'] = aposentar + 35
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')'''

#Guanabara
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho: (0 não tem) '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação']+ 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')