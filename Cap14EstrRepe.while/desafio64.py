# contabilizar todos os números e parar a contagem quando digitar 999

#minha resoluçao está funcional.
'''n1 = ''
contador = 0
soma = 0
while n1 != 999:
    n1 = int(input('Digite um número [999 para parar]: '))
    contador +=1
    soma += n1
print(f'Você digitou {contador - 1} números e a soma entre eles é de {soma - 999}')'''


#RESOLUÇÃO DO GUANABARA
num = cont = soma = 0 #nesse caso, como todas as variáveis estavam em zero, podia fazer isso.
num = int(input(('Digite um número [999 para parar: ]')))
while num != 999:
    soma += num
    cont += 1
    num = int(input(('Digite um número [999 para parar: ]')))
    #aqui guanabara apresenta um procedimento para não colocar a subtração 999
#colocou a variável primeira fora e depois as seguintes foi jogada por último dentro da while
#assim, o programa ler o flag (999) no lado de fora e no lado de dentro, na última linha
print(f'Você digitou {cont} e a soma entre eles é de {soma}')




