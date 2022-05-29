#super pa

'''primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1 #vai servir pra limitar o while
termo = primeiro
contagem = 0
while c <= 10:
    print(f'{termo}', end = ' ')
    termo += razao
    c += 1
    contagem += 1
    if c > 10:
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        c = 1
        while c <= 10 - mais:
            c += 1

print(f'fechou com {contagem} termos mostrados')
#minha resolução tem uma falha, pois, quando o número digitado é maior que dez, o mesmno, nao consegue apresentar mais de dez razão.

#resolução do guanabara.'''
primeiro = int(input('Termo inicial: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end = ' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('digite quantos termos a mais gostaria de ver: '))
print(f'Progressão finalizada com {total} termos mostrados')