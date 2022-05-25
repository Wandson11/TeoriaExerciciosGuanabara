#Criar um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0

#print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
while escolha != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    escolha = int(input('Qual é a sua opção? '))
    if escolha == 1:
        if n1 and n2:
            print(f'A soma entre {n1} e {n2}, é de {n1+n2}')
            print('=-=' * 20)
    elif escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é de {n1*n2}')
        print('=-=' * 20)
    elif escolha == 3:
        '''Aqui na aula, foi usada a seguinte sintaxe:
        if n1> n2:
        maior=n1
        else:
        maior = n2
        eu fiz direto usando o max, nao sei bem o pq dele nao ter usado, os das diferenças'''
        print(f'O maior número entre {n1} e {n2}, é o {max(n1, n2)}')
    elif escolha == 4:
        n1 = int(input('Digite o novo primeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    elif escolha == 5:
        print('Sair do programa')
    else:
        print('Número inválido')
print('Finalizado')

