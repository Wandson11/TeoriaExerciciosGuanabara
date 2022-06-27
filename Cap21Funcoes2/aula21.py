#para acessar o consele "python console".
#Interacrive Help , help()
#help(print)

#docstring, manual que informa sobre uma função ou cálculo, usa-se aspas duplas, 3 vezes;
'''def contador(i, f, p):
    """
    faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('Fim')
help(contador)'''

#argumentos(Parâmetros) opcionais
#caso o número de parametro for menor que o anunciado, dá para colocar um zero
# c= 0
'''def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 6, 8)
somar(1, 4)'''

# Escopo de variáveis
#onde uma variável vai existir e onde uma variável não vai mais existir.
#escopo global, tudo que tiver fora do def
#escopo local, tudo que tiver dentro do def.
'''def teste(b):
    global a #aqui, o A de fora será substituido pelo A de dentro
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')

a = 5
teste(a)
print(f'A fora vale {a}')'''

#retorn - Retorno de resultados
#bom para personalização de resultados
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,2 ,5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram: {r1}, {r2} e {r3}')'''

#prática
'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
#print(par(num))
if par(num):
    print('É par')
else:
    print('Impar')