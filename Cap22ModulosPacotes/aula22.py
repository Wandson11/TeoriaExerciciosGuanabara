#modularização
#Foco: dividir um programa grande; aumentar a legibilidade e facilitar a manutenção
#todo arquivo .py, pode ser entendido como modulo pelo sistema, desde que tenha funções internas

import uteis #para criar vinculos
#from uteis import fatorial, dobro (isso, não é tão recomendável pelo próprio python
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num) #para o vinculo dar certo, tem que inserir o titulo do arquivo de referência, no caso, uteis.
print(f'O fatorial de {num} e {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')#aqui mesma coisa

#vantagens: organização do código; manutenção; ocultação do código detalhado e reutilização em outros projetos
#pacote: como se fosse um pacote de módulos.
#caminho para criar um pacote: pythonteste > new > python package