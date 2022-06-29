#escrever um programa que rode um fatorial, onde é apresentado a possibilidade de mstrar a evlução do cálculo

'''def fatorial(v=1, show=True):
    """
    :param v: valor fatorial
    :param show: True ou False para mostrar o resumo do cáluclo fatorial
    :return: retorno os resultados
    """
    cont = 1
    if show == True:
        for c in range(v, 0, -1):
            print(f'{c}', end= ' ')
            print(' x ' if c > 1 else ' =', end= ' ')
            cont *= c
        return cont
    else:
        for c in range(v, 0, -1):
            cont *= c
        return cont
print(fatorial(3, show=False))'''

#Guanabara

def fatorial(n, show=False):
    """
    -> calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: Mostrar ou não conta
    :return: O valor fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c >1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f

print(fatorial(5, show=True))