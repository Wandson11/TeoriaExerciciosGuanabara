#escreva um programa que leia a velocidade de um carro
# se ultrapassar 80km, mostre uma msg dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite

zum = float(input('Velocidade máxima atingida: '))
multa = ((zum - 80) * 7.0)
if zum >= 80:
    print(f'Você foi multado por ter atingido velocidade acima do permitido, multa de R$ {round(multa,2)}')
else:
    print('')
  # ficou funcional igual ao da aula mas a estrutura feita foi de forma diferente (condiçao simples)
