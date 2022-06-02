#mostre a tabuada de vários números.
#programa será interrompido quando der valor negativo.

# está funcional, fiz usando o for
'''tabuada = conta = 0
c = ''
while True:
    print('-=-' * 20)
    tabuada = int(input('Qual será a tabuada? '))
    if tabuada < 0:
        break
    for c in range(1, 11):
        conta = c * tabuada
        print(f'{tabuada} x {c} = {conta}')

print('fim')'''

#essa versao sera com o while

c = 0
while True:
    tabuada = int(input('Qual será a tabuada? '))
    if tabuada < 0:
        break
    while c < 10:
        c += 1
        multiplicacao = c * tabuada
        print(f'{tabuada} x {c} = {multiplicacao}')
    c = 0 #sem isso daqui, a contagem não se reinicia, pois ao digitar o segundo valor a variavel tabuada aparece de novo
    #assim, com o c=0, ele reinicia. Vi nos comentários essa sintaxe do c=0
    #outro ponto,
#outro ponto importante é o local do c+=1, pois se for colocado ao final, nao vai registrar todos os 10 valores
#ainda, tem que se atentar ao c=0 e ao c<10
print('Fim')