#mostrar uma contagem regressiva para o estouro de fogos de artificio, indo de 10 a 0, com uma pause de 1 s.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Pow')
#foi usado a funçao sleep, importado da biblioteca time

