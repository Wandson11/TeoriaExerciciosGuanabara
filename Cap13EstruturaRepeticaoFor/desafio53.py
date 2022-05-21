#detector de palíndromo

'''n1 = str(input('Digite uma frase: ')).upper()
conjunto = ['APOS A SOPA', 'A SACADA DA CASA', 'A TORRE DA DERROTA', 'O LOBO AMA O BOLO', 'ANOTARAM A DATA DA MARATONA']
inverso = n1[::-1]
print(f' Voce digitou {n1.replace(" ","")}, que ao contrário, significa {inverso.replace(" ", "")}')
for n1 in conjunto:
    print(f'a {"APOS A SOPA" in n1}')'''

#nao consegui resolver esse desafio.

#resoluçao do guanabara
frase = str(input('Escreva uma frase: ')).upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#dá para fazer sem o for, no caso, uso o inverso = junto[::-1], essa ideia cheguei a usar no meu modelo.
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('temos um palíndromo')
else:
    print('Nao é um palíndromo')
    
    #resoluçao enxuta que vi nos comentários

'''frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")'''




