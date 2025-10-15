# Positivos e média

quantPositivos = 0
soma = 0

for num in range(6):
    numero = float(input())
    if numero > 0:
        quantPositivos += 1
        soma += numero

media = soma / quantPositivos

print("{:.0f} valores positivos".format(quantPositivos))
print("{:.1f}".format(media))