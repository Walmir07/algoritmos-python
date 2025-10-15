# Pares, ímpares, positivos e negativos

pares = 0
impares = 0
positivos = 0
negativos = 0

for num in range(5):
    numeros = int(input())

    if numeros % 2 == 0:
        pares += 1

    if numeros % 2 != 0: 
        impares += 1

    if numeros > 0:
        positivos += 1
        
    if numeros < 0:
        negativos += 1

print("{:.0f} valor(es) par(es)".format(pares))
print("{:.0f} valor(es) impar(es)".format(impares))
print("{:.0f} valor(es) positivo(s)".format(positivos))
print("{:.0f} valor(es) negativo(s)".format(negativos))