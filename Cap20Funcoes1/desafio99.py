#programa que tenha a função maior que receba vários parâmetros com valores inteiros
#programa vai apontar, qual desses valores é o maior.

'''def maior(*valores):
    print('~' * 20)
    for c in valores:

        print(f'{c} ', end=' ')
    print('Fim')

    print(f'O maior valor da lista acima é {max(valores)}')

maior(5, 0, 1, 4)
maior(8, 3, 6, 1)
maior(5, 1, 7, 9, 0)
maior()'''

'''def maior(* num):
    print('-' * 60)
    if len(num) > 0:
        print(f'Os numeros informados foram:', end='')
        for n in num:
            print(f' {n}', end='')
        print(f'. Foram informados {len(num)} ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('A função não recebeu valores.')
maior(5, 0, 1, 4)
maior(8, 3, 6, 1)
maior(5, 1, 7, 9, 0)
maior()'''


#Guanabara

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 6, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior()