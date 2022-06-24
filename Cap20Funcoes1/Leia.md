O novo capítulo apresenta os conceitos de funçoues aplicadas, essencialmente, quando um código vira rotina.
Dessa forma, essas funçoes podem ser executadas em momentos distintos do processo, automatizando códigos e economizando tempo.
Para fazer referência a criação de uma funçao, aplica-se o "def" com a variável e seus parâmetros.
Quando o parâmetro é texto, pode ser escrito assim: def título(txt), ou seja, dentro dos parenteses, aplica-se o "txt".
Quando o parametro é número, pode ser escrito assim: def contador(*num), ou seja, entre os parenteses, insere o sinal de multiplicação e "Num".

Modelo de def texto:
ef título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
#para rodar texto, colocar entra os parenteses o codigo: txt
título('Curso em vídeo')
título('Aprenda Python')
título('Oi')

Modelo de def número: 
def contador(*num):
    print(f'{num} ', end=' ')
    print('fim')
    for c in num:
        print(f'{c} ', end=' ')
    print('fim')
    tam = len(num)
    print(f'Recebi os valores {num}, que são ao todo {tam} números')

contador(3, 4, 7, 5)
contador(1, 8)
contador(2, 6, 9)
