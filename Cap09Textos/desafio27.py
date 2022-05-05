#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome

#não consegui fazer o último
'''n = str(input('Digita seu nome completo: '))
separado = n.split()
print(f'Primeiro nome: {separado[0]}')
print(f'último nome: {separado[:]}')'''

#resposta da aula do guanabara
n = str(input('Digito seu nome completo: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
#com as alteraçoes de 2019, essa linha de cima pode ser escrita assim: print(f'Seu último nome é {nome[-1]}')
#no comentários do vídeo, é indicado que o menos -1, inverte a ordem: Peixe(-3) Boi (-2) Azul (-1)
