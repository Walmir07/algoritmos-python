# Seis Números Ímpares

x = int(input())
contador = 0

while contador < 6:
    if x % 2 == 0:
        x += 1
    print(x)
    x += 2
    contador += 1
