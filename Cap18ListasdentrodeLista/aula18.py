'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])#aqui, se nao fizer a cópia com :, a reproduçao só vai mostrar maria, 22
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Joao', 19], ['Anna', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
for p in galera:
    print(p[0])# aqui, se o colchete, mostra a lista por linha, com conhece, filtra em nome ou idade'''

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite a sua idade: ')))
    galera.append(dado[:])#aqui, tem que fazer cópia, caso contrário, o clear abaixo, vai limpar tudo
    dado.clear()
#print(galera)

for p in galera:
    if p[1] >= 21: #aqui,outro observação, filtrar com o colchete a idade
        print(f'{p[0]} é maior de idade')

