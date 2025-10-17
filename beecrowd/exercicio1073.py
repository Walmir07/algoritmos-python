# Quadrado de Pares

n = int(input())

for i in range(2, n + 1, 2):

    potencia = i ** 2

    if n % 2 == 0:
        print("{:.0f}^2 = {:.0f}".format(i, potencia))
