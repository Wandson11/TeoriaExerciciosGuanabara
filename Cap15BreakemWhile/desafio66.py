#digite valores até que seja interrompido e ao final, apresente quantos números foram digitados e o seu somatório

numero = int(input('Digite um número: [999 para a contagem]: '))
somatório = quantidade = 0

while True:
    somatório += numero
    quantidade += 1
    numero = int(input('Digite um número: [999 para a contagem]: '))
    if numero == 999:
        break
print(f'A soma de {quantidade} valores foi de {somatório}')