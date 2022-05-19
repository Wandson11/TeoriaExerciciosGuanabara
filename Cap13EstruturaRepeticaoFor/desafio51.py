#programa para ler o primeiro termo da razão de uma PA, no final, mostrar os 10 primeiros termos da progressão

'''print('=' * 30)
print('10 Termos de uma PA')
print('=' * 30)

n1 = int(input('Digite o termo inicial: '))
n2 = int(input('Digite a razão: '))

primeiro = n1
pac = n2
ultimo = n2 * 10
for c in range(primeiro, ultimo, pac):
    print(c, end = '->')
print('Acabou')'''
#no caso, funcional, mas quando colocar números alto na razao, nao conta até 10, esqueci do enésimo termo de uma pa
#soluçao abaixo, repassado em aula.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end = '->')
print('Acabou')