produto = float(input('Qual é o preço do produto? R$ '))
desconto = produto * 0.05
print(f'O produto que custava {produto}, na promoção com desconto de 5% vai custar R$ {round(produto - desconto, 5)}')
