#programa que tenha funçao chamada escreva,
#que recebe um texto qualquer como parâmetro
#e mostre uma msg com tamanho adaptável

'''def escreva(txt):
    print(f'-' * len(txt))
    print(txt)
    print(f'-' * len(txt))


escreva('Teste do desafio 97')
escreva('Aula do curso em vídeo')
escreva('Oi')'''

#Guanabara
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Curso em vídeo')
escreva('Cev')
