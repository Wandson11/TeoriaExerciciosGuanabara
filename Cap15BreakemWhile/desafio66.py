#digite valores até que seja interrompido e ao final, apresente quantos números foram digitados e o seu somatório

'''numero = int(input('Digite um número: [999 para a contagem]: '))
somatório = quantidade = 0

while True:
    somatório += numero
    quantidade += 1
    numero = int(input('Digite um número: [999 para a contagem]: '))
    if numero == 999:
        break
print(f'A soma de {quantidade} valores foi de {somatório}')'''

soma = cont = 0
while True:
    num = int(input('Digite um valor: 999 pra parar: '))
    cont += 1
    soma += num
    if num == 999:
        break

print(f'Foram digitados {cont} que somados perfazem o valor de {soma}')
