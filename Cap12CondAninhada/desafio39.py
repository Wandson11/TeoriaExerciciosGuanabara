#programa que leia o ano de nascimento do jovem, e informe, de acordo com sua idade, se:
# se ainda vai se alistar;
# se é hora de se alistar;
# ou se ja passou do tempo;
#mostrar o tempo que falta para se alistar ou o tempo que já passou.

#feito sem import date, está funcional
'''ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
aindavaialistar = 18 - idade
alistamentopassado = idade - 18
print(f'Quem nasceu em {ano}, tem {idade} anos')
if idade < 18:
    print(f'Ainda falta(m) {aindavaialistar} ano(s) para se alistar')
elif idade == 18:
    print(f'Esse é o ano de você se alistar, pois tem {idade} anos')
else:
    print(f'Era para você ter se alistado a {alistamentopassado} ano(s)')'''

#minha resolução do exercício, ja que no de cima, a premisa do exemplo foi diferente.
'''nascimento = int(input('Digite o ano de nascimento: '))
idade = 2022 - nascimento
alistar = 18 - idade
anodoalistamento = (nascimento + 18)
print(f'Quem nasceu em {nascimento} tem {idade} anos em 2022')
if idade < 18:
    print(f'Ainda falta(m) {alistar} ano(s) para o alistamento')
    print(f'Seu alistamento será em {anodoalistamento}')
elif == 18:
    print('Voce está em idade para se alistar')
else:
    jafoi = idade - 18
    print(f'Você já deveria ter se alistado há {jafoi} ano(s)')
    jasealistou = nascimento + 18
    print(f'Seu alistamento foi em {jasealistou}')'''

#resolução do guanabara
from datetime import date
atual = date.today().year #usando esse código para chamar o presente ano.
nascimento = int(input('Data de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    alistar = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda falta(m) {alistar} para o alistamento')
    datafuturo = atual + alistar
    print(f'Seu alistamento será em {datafuturo}')
else:
    alistou = idade - 18
    datapassado = atual - alistou
    print(f'Você já deveria ter se alistado a {alistou} ano(s)')
    print(f'Seu alistamento foi em {datapassado}')