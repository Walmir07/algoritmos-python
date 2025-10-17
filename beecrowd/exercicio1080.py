# Maior e posição

maior = 0
posicao = 0

for num in range(1, 101):
    numero = int(input())

    if numero > maior:
        maior = numero
        posicao = num

print(maior)
print(posicao)
