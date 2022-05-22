#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo;
# qual é o nome do homem mais velho;
# quantas mulheres têm menos de 20 anos.

'''mediaidade = 0
idoso=0
somamulher = 0
listahomem = 0

for c in range(1,5):
    print(f'======== {c}ºPessoa ========')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    mediaidade += idade
    if c ==1:
        idoso = idade
    else:
        if idade > idoso:
            idoso = idade

    sexo = str(input('[M/F]: '))
    if sexo == "f":
        if idade < 20:
            somamulher += 1
    elif sexo == "m":
        if idoso == idade:
            listahomem = nome
print(f'A média de idade do grupo é de {mediaidade/4}')
print(f'O homem mais velho tem {idoso} e se chama {listahomem}')
print(f'O total de mulheres com menos de 20 anos é de {somamulher}')'''

#resoluçao ficou parecida com o do guanabara, mas reproduzi a resposta por causa de umas diferenças

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): '))
    somaidade += idade
    if c == 1 and sexo in 'Mm': #aqui usou o sexo in 'mM', para poder selecionar os dois Ms.
        maioridadehomem = idade
        nomevelho = nome #outra diferença, jogou logo aqui o nome do + velho.
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo sao {totmulher20} com menos de 20 anos')
