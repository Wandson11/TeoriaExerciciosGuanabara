#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

#essa foi a primeira versão
'''nome = str(input('Digite seu nome completo: '))
print('Silva' in nome)'''

#ajustei posteirormente para isso, no caso inseri title para padronizar a leitra dos nomes, conforme a aula.
#na aula usuou exemplo como lower e upper
#mas novamente não está perfeito, pois reconhece "silvana" como True
'''nome = str(input('Digite seu nome completo: ')).strip()
print('Silva' in nome.title())'''

#agora correto
nome = str(input('Digite o seu nome completo: ')).strip()
nomealterado = nome.upper().split()
print('SILVA' in nomealterado[:])
