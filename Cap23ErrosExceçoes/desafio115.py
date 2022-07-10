import desafio115a
import desafio115barquivo
from time import sleep

arq = 'cursoriness.txt'

if not desafio115barquivo.arquivoExiste(arq):
    desafio115barquivo.criarArquivo(arq)

while True:
    resposta = desafio115a.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opcao de listar o conteudo de um arquivo
        desafio115barquivo.lerArquivo(arq)
    elif resposta == 2:
        desafio115a.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = desafio115a.leiaInt('Idade: ')
        desafio115barquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        desafio115a.cabecalho('Saindo do sistema...até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
