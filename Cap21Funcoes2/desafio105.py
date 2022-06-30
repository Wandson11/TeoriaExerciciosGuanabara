#ter uma função notas com varias notas de alunos, onde será retornado um dicio
#apresentado as seguintes informações:
#qtde de notas; a maior nota, menor nota; média e situaçao

'''def notas(*num, sit=False):
    """
    :param num: aqui compila as notas digitadas em um unico ponto
    :param sit: se false, não apresenta a situação, se verdadeiro apresenta se foi boa, razoável ou ruim
    :return: retorno o resultado do dicionário compilando os valores pedidos
    """
    dicionário = {}
    dicionário['quantidade'] = len(num)
    dicionário['maior'] = max(num)
    dicionário['menor'] = min(num)
    dicionário['media'] = sum(num) / len(num)
    if dicionário['media'] >= 7:
        dicionário['situação'] = 'Boa'
    elif dicionário['media'] >= 5 and dicionário['media'] < 7:
        dicionário['situação'] = 'Razoável'
    else:
        dicionário['situação'] = 'Ruim'
    return dicionário


resp = notas(4.8, 4.5, 4.5)
print(resp)'''

#Guanabara
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit: #aqui é apresentado o sit
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r

resp = notas(5.5, 2.5, 2.5)
print(resp)