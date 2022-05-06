# Crie um programa que leia o nome completo de uma pessoa e mostre

#minha resolução
'''nome = str(input('Digite o seu nome: '))
print(f'Todas as letras maiúsculas {nome.upper()}')
print(f'Todas as letras minúsculas {nome.lower()}')
cortaespaco = nome.split()
sumindocomespaco = nome.replace(" ", "")
contagemsemespaco = len(sumindocomespaco)
print(contagemsemespaco)
print(f'Quantas letras tem o primeiro nome? {len(cortaespaco[0])}')'''

#resolução da aula
nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu nome é maiúscula é {nome.upper()}')
print(f'Seu nome é minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
# print(f'Seu primeiro nome tem {nome.find(" ")} letras') o índice começa pelo zero
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')
