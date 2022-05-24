#programa que leia o sexo da pessoa, mas só aceite valores M e F.
# caso digitem errado, peça a digitação novamente, até que acerte.


'''s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite o sexo: [F/M] ')).upper()
    if s == 'F' or s == 'M':
        print(f'Cadastrado')'''

#resoluçao Guanabara
sexo = str(input('Digite o sexo: [F/M]: ')).strip().upper()[0]#esse último, em caso da pessoa digitar o nome inteiro, o programa vai pegar somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo}, cadastrado com sucesso')

#aqui ficou claro a inclusão do maiúsculo e minúsculo 'MmFf'


