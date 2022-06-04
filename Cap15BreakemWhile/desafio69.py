#cadastrar pessoas, com opção de continuar cadastrando.
'''adulto = 0
masculino = 0
mulher20 = 0
while True:
    print('-=-' * 20)
    print('Cadastre uma pessoa')
    print('-=-' * 20)
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        adulto += 1
    sexo = str(input('Digite o sexo: ')).upper()[0]
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F' and idade <= 20:
        mulher20 += 1
    while sexo not in "FM":
        print('Inválido, digite novamente')
        sexo = str(input('Digite o sexo: ')).upper()[0]
    print('-=-' * 20)
    novos = str(input('Quer continuar: [S/N] ')).upper()[0]
    if novos == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {adulto}')
print(f'Ao todo, tem-se {masculino} homem (ns) cadastrados ')
print(f'E temos {mulher20} mulher(es) com menos de 20 anos')'''

#resolução do guanabara
tot18 = toth = totmulher20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o sexo: [F/M]: ')).strip().upper()[0]
    if idade > 18:
        tot18 +=1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade <20:
        totmulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tot18} homens cadastrados')
print(f'Temos um {totmulher20} mulheres com menos de 20 anos')