# Pares entre cinco números

pares = 0

for num in range(5):
    numeros = int(input())
    if numeros % 2 == 0:
        pares += 1

print("{:.0f} valores pares".format(pares))