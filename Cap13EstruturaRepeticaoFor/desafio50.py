#ler seis números inteiros e mostre a soma apenas daqueles que forem pares.

qtde = 0
soma = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n #vai somar apenas os números impar e dar um total do somatório
        qtde += 1 # vai somar a quantidade de números impares
print(f'A quantidade de números pares foi de {qtde} e o somatório de seus números foi de {soma}')

#minha resposta ficou parecida com o do Guanabara

