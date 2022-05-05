# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome de 'santo'

#funciona bem mas não perfeitamente, pois Santos e santorini, dão como True
'''local = str(input('Digite o nome de uma cidade: ')).strip()
separando = local.split()
primeironome = separando[0]
print('Santo' in primeironome.title())'''

#Modelo da aula, tbem dá o mesmo erro que o meu de cima.
'''cid = str(input('Digite o nome de uma cidade: ')).strip()
print(cid[:5].upper() == "SANTO")'''

#exemplo que peguei no video e que funciona certo
n = input('Digite o nome da cidade: ').strip().split()
print(n[0].upper() == "SANTO")
