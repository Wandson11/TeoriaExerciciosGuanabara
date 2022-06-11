#uma tupla com várias palavras, em que será demonstrado as vogais de cada palavra

#deu para fazer de forma parcial, não consegui configurar de forma correta.
'''palavras = ('estudo', 'linguagem', 'programar', 'python', 'rotina', 'desafio', 'tarefa',
            'persistencia', 'teste', 'gambiarra')
vogais = ('a', 'e', 'i', 'o', 'u') #aqui pensei em usar algo como find para apresentar as vogais do c, nao deu certo.
for c in palavras:
    print(f'Na palavra {c}, tem-se as seguintes vogais: ', end=' ')
    if "a" in c:
        print('a')
    if "e" in c:
        print('e')
    if "i" in c:
        print('i')
    if "o" in c:
        print('o')
    if "u" in c:
        print('u')'''
#para quebrar a linha, bastava colocar antes de cada "c" o \n
#Guanabara

palavras = ('estudo', 'linguagem', 'programar', 'python', 'rotina', 'desafio', 'tarefa',
            'persistencia', 'teste', 'gambiarra')

for p in palavras:
    print(f'\nNa palavra {p}, temos ', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
