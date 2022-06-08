#fazer um prg que tenha uma tupla preenchida de 0 a 20, de forma extensa.
# o programa deve ler o numero digitado e apresentar o valor por extenso.


extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
numero = 0

if numero < 11:
    numero = int(input('Digite um número entre 0 e 10: '))
    while numero >= 11 or numero < 0:
        numero = int(input('Inválido, tente novamente, Digite um número entre 0 e 10: '))
    print(extenso[numero])

print('Fim')


