'''def metade(preco=0, formato=False):
    resposta = preco/2
    return resposta if formato is False else moeda(resposta)

def dobro(preco=0, formato=False):
    resposta = preco*2
    return resposta if formato is False else moeda(resposta)

def aumentar(preco=0, taxa=0, formato=False):
    resposta = preco + (preco * taxa/100)
    return resposta if formato is False else moeda(resposta)

def diminuir(preco=0, taxa=0, formato=False):
    resposta = preco - (preco*taxa/100)
    return resposta if formato is False else moeda(resposta)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxamaior=0, taxamenor=0):
    titulo = 'Resumo do Valor'
    print('=-=' * len(titulo))
    print(f'{titulo:^40}')#aqui, pode ser usado assim: 'resumo do valor'.center(30), esse 30, foi aleatório
    print('=-='*len(titulo))
    print(f'Preco Analisado{moeda(preco):>20}')
    print(f'Dobro do Preço {dobro(preco, True):>20}')
    print(f'Metade do Preço{metade(preco, True):>20}')
    print(f'{taxamaior}% de Aumento {aumentar(preco, taxamaior, True):>20}')
    print(f'{taxamenor}% de Redução {diminuir(preco, taxamenor, True):>20}')'''

#DETALHE IMPORTANTE, PARA DEIXAR A TABELA FORMATADA, É SO USAR \t ANTES DAS CHAVES SEM A FORMATAÇÃO A DIRETA.
def metade(preco=0, formato=False):
    resposta = preco/2
    return resposta if formato is False else moeda(resposta)

def dobro(preco=0, formato=False):
    resposta = preco*2
    return resposta if formato is False else moeda(resposta)

def aumentar(preco=0, taxa=0, formato=False):
    resposta = preco + (preco * taxa/100)
    return resposta if formato is False else moeda(resposta)

def diminuir(preco=0, taxa=0, formato=False):
    resposta = preco - (preco*taxa/100)
    return resposta if formato is False else moeda(resposta)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxamaior=0, taxamenor=0):
    titulo = 'Resumo do Valor'
    print('=-=' * len(titulo))
    print(f'{titulo:^40}')#aqui, pode ser usado assim: 'resumo do valor'.center(30), esse 30, foi aleatório
    print('=-='*len(titulo))
    print(f'Preco Analisado \t{moeda(preco)}')
    print(f'Dobro do Preço \t\t{dobro(preco, True)}')
    print(f'Metade do Preço \t{metade(preco, True)}')
    print(f'{taxamaior}% de Aumento \t\t{aumentar(preco, taxamaior, True)}')
    print(f'{taxamenor}% de Redução \t\t{diminuir(preco, taxamenor, True)}')