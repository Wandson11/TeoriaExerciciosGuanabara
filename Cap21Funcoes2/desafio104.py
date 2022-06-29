#uma programa que tenha leiaint(), onde somente vai passar pela formula
#se tiver numero digitado, do contrario, pedira um número inteiro.

'''def leiaint(valor):
   teste=input(valor)
   if teste.isnumeric():
       return teste
   else:
       print(f'Valor inválido, digite novamente {valor}')
       return teste


n= leiaint('Digite um número: ')
print(f'O número digitado foi {n}')'''

''''#Guanabara
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro váludo.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')'''

def leiaint(valor):
    if n.isnumeric():
        return
    elif n.isalpha():
        print('Digite novamente, pois nao foi escrito um número')


n = str(input('Digite um valor: '))
print(f'O número digitado foi {n}')




