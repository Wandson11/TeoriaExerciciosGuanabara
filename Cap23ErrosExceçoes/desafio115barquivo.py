import desafio115a

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #esse mais, vai criar um pastaou aba, para inserir os valores digitados.
        a.close()
    except:
        print('Houve um erro na criacao do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        desafio115a.cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print(f'Houve um erro na hora escrever')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
