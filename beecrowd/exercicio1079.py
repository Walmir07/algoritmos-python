# Médias ponderadas

n = int(input())

for i in range(n):
    nota1, nota2, nota3 = input().split()

    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)

    peso1 = 2
    peso2 = 3
    peso3 = 5

    mediaPonderada = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)

    print("{:.1f}".format(mediaPonderada))