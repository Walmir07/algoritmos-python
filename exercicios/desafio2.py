numericos = []

for i in range(5):
    numero = int(input("Digite o número: "))
    numericos.append(numero)

numericos.sort(reverse=True)

print(*numericos, sep="\n")

tamanhoLista = len(numericos)
elementoDoMeio = int((tamanhoLista - 1) / 2)

print(f"O elemento do meio é {numericos[elementoDoMeio]}")