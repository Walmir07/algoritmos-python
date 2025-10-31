# Troca em vetor I

lista = []

for i in range(5):
    lista.append(int(input()))

listaInvertida = lista[::-1]

for j in listaInvertida:
    print(f"N[{listaInvertida.index(j)}] = {j}")
