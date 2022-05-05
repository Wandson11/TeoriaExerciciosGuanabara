#faça um programa que leia um frase pelo teclado e mostre

#não consegui fazer o último
'''n = str(input('Digite uma frase: ')).strip().upper()
contagem = n.count('A')
print(f'Quantas vezes aparece a letra "a"? {contagem}')
primeira = n.find('A')
print(f'Em que posiçao ela aparece a primeira vez? {primeira}')
print(f'Em que posiçao ela aparece pela última vez? {primeira}')'''

#modelo da aula, usou no último o rfind (nem sabia que dava pra fazer isso)
n = str(input('Digite uma frase:')).upper().strip()
print(f'A letra "A" aparece {n.count("A")} vezes')
print(f'A primeira letra "a" apareceu no índice {n.find("A")}')
print(f'A última letra "a" apareceu no índice {n.rfind("A")}')
