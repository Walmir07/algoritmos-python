# Preenchimento de vetor I

vetor = []
valor = int(input())


for i in range(10):

    vetor.insert(0, valor)

    print(f"N[{i}] = {vetor[i]}")

    vetor[i] *= 2
    