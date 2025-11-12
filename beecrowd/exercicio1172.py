# Substituição de vetor I

vetor = []

for i in range(10):
    vetor.append(int(input()))

    if vetor[i] == 0 or vetor[i] < 0:
        vetor[i] = 1

    print(f"X[{i}] = {vetor[i]}")