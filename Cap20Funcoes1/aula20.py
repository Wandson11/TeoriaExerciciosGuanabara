'''def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
#para rodar texto, colocar entra os parenteses o codigo: txt
título('Curso em vídeo')
título('Aprenda Python')
título('Oi')'''

#Parte prática.
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

#os parametros da soma, tem que ser equivalente, se tiver um só e a formula pedir 2, dará erro.
soma(4, 5) #soma(a=4, b=5) ou soma(b=4, a=5)
soma(9, 8)
soma(2, 1)'''

'''def contador(*num):
    print(f'{num} ', end=' ')
    print('fim')
    for c in num:
        print(f'{c} ', end=' ')
    print('fim')
    tam = len(num)
    print(f'Recebi os valores {num}, que são ao todo {tam} números')

contador(3, 4, 7, 5)
contador(1, 8)
contador(2, 6, 9)'''

#com lista
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [3, 6, 1, 4, 7, 0]
dobra(valores)
print(valores)'''

#desempacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')


soma(5, 2)
soma(4, 9, 2)

