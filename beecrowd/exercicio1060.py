# Números positivos:

positivos = 0

for num in range(6):
    valor = float(input())
    if valor > 0:
        positivos += 1

print(f"{positivos} valores positivos")
