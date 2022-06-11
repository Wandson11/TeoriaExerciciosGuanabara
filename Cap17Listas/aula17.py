#vai inserir mais um elemento na lista, porém na última casa
#variavel.append('qualquer coisa')

#escolher em qual indice será inserido novo elemento.
#variavel.insert(k, 'nome')

#excluir um elemento.
#del lanche[numero]
#lanche.pop(3)
#lanche.remove('nomedo elemento, pizza, por exemplo')

#valores.sort - coloca em ordem do menor para o maior
#lembrando que sorted - coloca em ordem alfabética.
#para colocar em ordem reversa, do maior para menor: valores.sort(reverse=True)

'''num = [2, 5, 9, 1]
num[3] = 8
num.append(7)
num.sort(reverse=True)
num.insert(0, 8) #aqui, o mesmo substitui por 8 o elemento que estiver no index 0
num.remove(8) #no modelo, caso existam dois numeros iguais, o que vier antes na contagem será removido.
#num.pop(3)
print(num)'''

#lista mais bonita
'''valores = []
# valores = list(), tanto faz com o de cima
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): #ao inves do range, esse for é para cada elemento da lista, no caso, os append.
    #enumerate, pega tanto a chave "c"(indice) quanto o valor
    print(f'Na posiçao {c} encontrei o valor {v}...')'''

'''valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    
for c, b in enumerate(valores):
    print(f'No elemento {c}, foi verificado o valor {b}')'''

a = [2,3,4,7]
#b=a #quando as listas sao unidas, o python, faz essa ligaçao e se alterar o b, vai alterar o a.
b = a [:]#dessa forma, os valores de a, serao repassados ao b, sem fazer a ligação, fazendo uma cópia
b[2] = 5
print(f'Lista a {a}')
print(f'Lista b {b}')
