# distancia de uma viagem em km, preço da passagem, R$ 0,50/km para te 200 km e 0,45 para mais longas

distancia = float(input('Qual é a distancia? '))
if distancia <= 200:
    print(f'O preço da passagem será R$ {distancia * 0.50}')
else:
    print(f'O preço da passagem será de R$ {distancia * 0.45}')
