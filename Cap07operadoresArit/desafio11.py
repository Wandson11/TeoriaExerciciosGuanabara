# apurar o tamanho de uma parede e a quantidade de tinta necessária para pinta-la

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
tim = 2
print(f'Sua parede tem a dimensao de {altura} x {largura} e sua área é de {altura * largura}m²')
print(f'Para pintar essa parede, voce precisara de {(altura * largura)/ tim}L de tinta')
