# calcular a soma entre todos os números ímpares que são múltiplos de 3
#e que estão no intervalo de 1 a 500.

#esse nao consegui fazer. travei em unir a sintaxe do múltiplos de 3 com o código.

'''n = 0
for c in range(1, 501):
    if c % 2 == 1 and c / 3 == 0 :
        if (c * 3) % 3:
            print(c, end = ' ')
        n += c
print(f'a soma é {n}', end = ' ')'''

#resoluçao do Guanabara
'''soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(f'A soma é de {soma}')'''
#importante, como se nota, eu errei na divisão, pois coloquei " / ", sendo que o correto era " % ".
#Outro ponto importante, é que foi colocado o dois logo em cima, e nao como IF, igual eu fiz.

soma = 0
contagem = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contagem = contagem + 1
print(f'A soma é de {soma} de um total de {contagem}')

