# contabilizar todos os números e parar quando for digitado N

#fiz estava funcional, mas não consegui adequar em colocar o menor número digitado.
'''n1 = 0
soma = 0
contador = 0
continuar = 'S'
maior = n1
menor = n1
while continuar == 'S':
    n1 = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? ')).strip().upper()[0]
    contador +=1
    soma += n1
    if n1 > maior:
        maior = n1
    else:
        menor = n1

média = soma / contador
print(f'Você digitou {contador} números é a média é de {média}')
print(f'O maior valor digitado foi de {maior} e o menor foi {menor}')'''

#resposta guanabara
resp = 'S'
soma = quant = media = maior = menor = 0 #diferença no meu, eu coloquei maior e menor igual a n1
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1: #aqui, o quant é resultado no 1, para remeter ao primeiro valor digitado
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar: [S|N]: '))
media = soma / quant
print(f'Você digitou {quant} é a média {media}')
print(f'o maior foi {maior} e o menor foi {menor}')
