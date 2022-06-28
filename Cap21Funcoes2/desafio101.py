#programa com função voto, que tenha parametro
# onde é digitado o ano de nascimento
# e como resposta, o return dará se o voto é opcional, obrigatório ou se não vota.

'''from datetime import datetime

def voto(v):
    hj = datetime.today().year
    calculo = hj - v
    if calculo < 18:
        return print(f'Não vota')
    elif 18 <= calculo <= 65:
        return print('Voto obrigatório')
    else:
        return print('Voto opcional')
v = int(input('Ano de nascimento: '))
voto(v)'''

#Guanabara
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto obrigatório'

nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))


