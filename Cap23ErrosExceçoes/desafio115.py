print('''
01 - Ver pessoas cadastradas
02 - Cadastrar nova pessoa
03 - Sair do sistem''')

import desafio115a
c=0
escolha = int(input('Qual é a opção? '))
while True:
    if escolha == 1:
        print('texto')
        c +=1
    elif escolha == 2:
        nome = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))


print()
