#programa que tenha uma funçao chamada area retangular (largura e comprimento)
#ao final, mostrar a área do terreno


'''print('Controle de Terreno')
print('-'*20)


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m) '))


def terreno(largura, comprimento):
    calculo = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {calculo}m²')
terreno(largura, comprimento)'''

#Guanabara
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}')


print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m) '))
c = float(input('COMPRIMENTO (m) '))
área(l, c)