'''for c in range(1, 10):
    print(c)
print('Fim')'''

#diferença entre os dois, é que no FOR, sabe-se o início e o seu limite, enquanto, quando você não tem essa info, é melhor usar o while

'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''

'''n = 1
while n !=0: # flag ou condição de parada
    n = int(input('Digite um número: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0: #aqui, tá usando o if para indicar que a saida 0, não vai contabilizar no print.
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print(f'São {par} par(es) e {impar} impar(es)')