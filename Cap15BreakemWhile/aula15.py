#aula 15

n = soma = 0

while True: #laço de forma infinita (looping)
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma do n é de {soma}')