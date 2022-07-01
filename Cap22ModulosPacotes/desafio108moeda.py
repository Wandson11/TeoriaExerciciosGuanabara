'''def moeda(valor):
    if valor >= 0:
        return f'R$ {valor}'

def metade(valor):
    resp = valor / 2
    return resp

def dobro(valor):
    resp = valor * 2
    return resp

def aumentar(valor, taxa):
    resp = valor + (valor * taxa/100)
    return resp

def reduzir(valor, taxa):
    resp = valor - (valor * taxa/100)
    return resp'''

def moeda(valor=0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')
    #aqui, eu tava colocando  :2f, sendo que o correto é :.2f

def metade(valor=0):
    resp = valor / 2
    return resp

def dobro(valor=0):
    resp = valor * 2
    return resp

def aumentar(valor=0, taxa=0):
    resp = valor + (valor * taxa/100)
    return resp

def reduzir(valor=0, taxa=0):
    resp = valor - (valor * taxa/100)
    return resp