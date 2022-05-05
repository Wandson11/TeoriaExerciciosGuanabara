#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

#tem falhas esse modelo que fiz, no caso, quando tem os 4 digitos, ele roda, mas virando centena, dezena ou unidade, o resultando do print dá errado
'''n = str(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {n[3:]}')
print(f'Dezena: {n[2:3]}')
print(f'Centena: {n[1:2]}')
print(f'Milhar: {n[:1]}')'''


#essa é a versão matemática, fiz consultando o google e ficou parecido com o da aula
n = int(input('Digite um número de 0 a 9999: '))
unidade = (n // 1) % 10
print(f'Unidade: {unidade}')
dezena = (n // 10) % 10
print(f'Dezena: {dezena}')
centena = (n//100) % 10
print(f'Centena: {centena}')
milhar = (n // 1000) % 10
print(f'Milhar: {milhar}')

