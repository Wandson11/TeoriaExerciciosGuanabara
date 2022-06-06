#fazer um caixa eletrônico



'''dinheiro = int(input('Que valor você quer sacar? '))

while True:
    conta = dinheiro // 100
    contadepoisdocem = dinheiro - (100 * conta)
    print(f'Em notas de cem reais, foram usadas {conta} cédulas, sobrando R$ {contadepoisdocem} reais')
    if contadepoisdocem == 0:
        break
    if contadepoisdocem > 0:
        tirandocinquenta = contadepoisdocem // 50
        contadepoisdocinquenta = contadepoisdocem - (50 * tirandocinquenta)
        print(f'Foram usadas {tirandocinquenta} cédula (s) de cinquenta reais')
    if contadepoisdocinquenta == 0:
        break
    if contadepoisdocinquenta > 0:
        tirandovinte = contadepoisdocinquenta // 20
        contadepoisvinte = contadepoisdocinquenta - (20 * tirandovinte)
        print(f'Foram usadas {tirandovinte} cédula(S) de vinte reais, sobrando {contadepoisvinte}')
    if contadepoisvinte == 0:
        break
    if contadepoisvinte > 0:
        tirandodez = contadepoisvinte // 10
        contadepoisdez = contadepoisvinte - (10 * tirandodez)
        print(f'Foram usada(s) {tirandodez} cédula(s) de dez reais, sobrando {contadepoisdez}')
    if contadepoisdez == 0:
        break
    if contadepoisdez > 0:
        tirandocinco = contadepoisvinte // 5
        contadepoiscinco = contadepoisdez - (5 * tirandocinco)
        print(f'Foram usada(s) {tirandocinco} cédula(s) de cinco reais, sobrando {contadepoiscinco}')
    if contadepoiscinco == 0:
        break
    if contadepoiscinco > 0:
        tirandodois = contadepoiscinco // 2
        contadepoisdois = contadepoiscinco - (2 * tirandodois)
        print(f'Foram usada(s) {tirandodois} cédulas de dois reais, sobrando {contadepoisdois}')
    if contadepoisdois == 0:
        break
    if contadepoisdois >= 1:
        tirandoum = contadepoisdois / 1
        contadepoisum = contadepoisdois - (1 * tirandoum)
        print(f'Foram usada(s) {tirandoum} cédula(s) de um real, sobrando {contadepoisum}')
    if contadepoisum == 0:
        break
print('Fim')'''

#teste
'''dinheiro = int(input('Que valor você quer sacar? '))
contador100 = contador50 = contador20 = contador10 = contador5 = contador2 = contador1 = 0
while True:
    while dinheiro - 100 >= 0:
        dinheiro -= 100
        contador100 += 1
    if contador100 != 0:
        print(f'Foram necessária(s) {contador100} cédula(s) de 100 reais')
    while dinheiro - 50 >= 0:
        dinheiro -= 50
        contador50 += 1
    if contador50 != 0:
        print(f'Foram necessária(s) {contador50} cédula(s) de 50 reais')
    while dinheiro - 20 >= 0:
        dinheiro -= 20
        contador20 += 1
    if contador20 != 0:
        print(f'Foram necessária(s) {contador20} cédula(s) de 20 reais')
    while dinheiro - 10 >= 0:
        dinheiro -= 10
        contador10 += 1
    if contador10 != 0:
        print(f'Foram necessária(s) {contador10} cédula(s) de 10 reais')
    while dinheiro - 5 >= 0:
        dinheiro -= 5
        contador5 +=1
    if contador5 != 0:
        print(f'Foram necessária(s) {contador5} cédula(s) de 5 reais')
    while dinheiro - 2>= 0:
        dinheiro -= 2
        contador2 += 1
    if contador2 != 0:
        print(f'Foram necessário(s) {contador2} cédula(s) de 2 reais')
    while dinheiro - 1>= 0:
        dinheiro -= 1
        contador1 += 1
    if contador1 !=0 :
        print(f'Foram necessário(s) {contador1} cédula(s) de 1 real')
    if dinheiro == 0:
        break'''
#Guanabara
valor = int(input('Qual o valor a ser sacado? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced#no ced, se jogar 50, o programa fica rodando infinitamente, por isso, é melhor a variável.
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 2
        elif ced == 2:
            ced = 1
        totalced = 0 #isso aaqui é importante, para evitar que acumule a contagem, assim reinicia sempre em um novo elif
        if total == 0:
            break
print('Obrigado pela preferência')

