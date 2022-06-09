#fazer um prg que tenha uma tupla preenchida de 0 a 20, de forma extensa.
# o programa deve ler o numero digitado e apresentar o valor por extenso.


'''extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
numero = 0

if numero < 11:
    numero = int(input('Digite um número entre 0 e 10: '))
    while numero >= 11 or numero < 0:
        numero = int(input('Inválido, tente novamente, Digite um número entre 0 e 10: '))
    print(extenso[numero])

print('Fim')'''

#acrescentando o continuar
'''extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
numero = 0

if numero < 11:
    numero = int(input('Digite um número entre 0 e 10: '))
    while numero >= 11 or numero < 0:
        numero = int(input('Inválido, tente novamente, Digite um número entre 0 e 10: '))
    print(extenso[numero])
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if continuar == 'S':
        numero = int(input('Digite um novo número entre 0 e 10: '))
        while numero >= 11 or numero < 0:
            numero = int(input('Inválido, tente novamente, Digite um número entre 0 e 10: '))
    print(extenso[numero])
print('Fim')'''

#resolução do guanabara

'''cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end= ' ')
print(f'Voce digitou o número {cont[num]}')'''


