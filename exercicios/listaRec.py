def potencia(a, b):

    if b == 0:
        return 1

    resultado = a * potencia(a, b - 1)

    return resultado

numero = int(input("Digite o número: "))
expoente = int(input("Digite o expoênte: "))

print(f"A potência de {numero} por {expoente} é: {potencia(numero, expoente)}")