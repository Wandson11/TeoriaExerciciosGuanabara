#Utilização de dicionários

'''dados =dict()
dados = {}
#append nao funciona
#para colocar um novo elemento
dados['sexo'] = 'M'
#para retirar um elemento
#del dados['Idade']
filme = {'titulo': 'Star Wars',
         'ANO': '1977',
         'Diretor': 'George Lucas'}
print(filme.values()) #vai retornar todos os dados acima, do star wars ao george lucas
print(filme.keys()) #vai retornar todos os indices, de título, ano e diretor
print(filme.items()) #puxa tudo
#esses 3 elementos acima, podem ser usados no for, igual um enumerate
#for k, v in filme.items():
#print(f'O {k} é {v}')
O tiutlo é star wars
O ano é 1977
O diretor é george lucas
#enumerates, usa-se nas tuplas e listas
#for em variavel.items, usa-se no dicionário
pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
pessoas['Nome'] = 'Leandro'#substitui gustavo por leandro
pessoas['Peso'] = 99 #adicionando elemento peso.
print(pessoas)

#dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

#exemplo
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #aqui, foi usado o copy, pois [:] não funciona direito para dicionário
for e in brasil:
    for v in e.values():
        print(v, end = ' ')
    print()