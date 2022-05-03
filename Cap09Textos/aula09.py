frase = 'Curso em Vídeo Python'

#Junção-----------------------
#no caso, o que tiver entre as aspas, sera usado, se não tiver nada, apresentará como está no exemplo acima.
#se tiver um traço -, ele vai aparecer entre todas as letras e espaços.
'''print(''.join(frase))'''


#Divisao---------------------------------------
#split, separa todas as palavras, formando assim, praticamente uma lista
#Isso acontece pq, quando uma palavra termina, ao invés do índice continuar a contagem, ele reinicia com nova palavra
#ainda, tira os espaços existentes na sua contagem.
'''print(frase.split())'''


#Transformação--------------------------------
#strip tira os espaços inúteis que podem ter antes ou depois da frase
'''print(frase.strip())'''
#tira os espaços inúteis no lado direito, quando tiver esses espaços no lado esquerdo é só colocar lstrip
'''print(frase.rstrip())'''
#title colocara letra maiúscula em toda nova palavra
'''print(frase.title())'''
#capitalize, basicamente coloca todas as letras minúsculas, menos a primeira, no C de Curso
'''print(frase.capitalize())'''
#coloca toda a frase com letras maiúsculas
'''print(frase.upper())'''
#coloca toda a frase com letras minúsculas
'''print(frase.lower())'''
#replace, vai trocar ou reposicionar a palavra da primeira aspa, igual ex abaixo:
'''print(frase.replace('Python', 'Android'))'''

#Análise -------------------------------------
#in é um procedimento booleano, te retornara com True ou False o que tiver dentro da aspa
'''print('Em' in frase)'''
#find indica o índice em que determinada letra ou palavra aparece, mas é o índice
'''print(frase.find('o'))'''
#count contara a quantidade de letra (tem que especificar, maiúscula ou minúscula), dentro das aspas do segundo parêntese.
'''print(frase.count('o'))'''
#mesclando lower com count
'''print(frase.lower().count('O'))'''
#len conta o total de espaço/índice ocupado pela frase, incluindo os espaços.
'''print(len(frase))'''



#fatiamento ---------------------------------
'''print(frase[::3])'''

#selecionar um texto (trecho) longo para o print, é só colocar 3 aspas duplas no inicio da frase e 3 no final
