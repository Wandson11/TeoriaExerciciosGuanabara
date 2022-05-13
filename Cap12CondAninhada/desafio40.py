#ler duas notas e calcular a média.
# média abaixo de 5.0: Reprovado
# Média entre 5.0 a 6.9: Recuperação
# me´dia maior que 7: aprovado

nota1 = float(input('Sua primeira nota: '))
nota2 = float(input('Sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi de {media} e você está reprovado')
elif media >= 5.0 and media < 6.9: # 7.0 > media >= 5.0: pode ser assim tbem
    print(f'Sua média foi de {media}, portanto, você está de recuperação')
elif media >= 7.0:
    print(f'Parabéns, sua média foi de {media}, você está aprovado')
#minha resposta ficou parecida com o do guanabara, mantive o que eu fiz.