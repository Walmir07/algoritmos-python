# 1°) Implemente a função fatorial recursiva. Crie um programa que use essa função.

def fatorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
numero = int(input("Digite o número: "))

print(f"O fatorial de {numero} é: {fatorial(numero)}")

# 2°) Implemente uma função recursiva que ache o menor valor em uma lista.Crie um programa que use essa função.

def menor(lista):

    if len(lista) == 1:
        return lista[0]
    
    menorValor = menor(lista[1:])

    if lista[0] < menorValor:
        return lista[0]
    
    return menorValor
    
lista = [21, 23, 12, 11]

print(f"O menor número da lista é: {menor(lista)}")

# 3°) Implemente uma função que calcule recursivamente uma potência de A elevado a B usando multiplicação. Crie um programa que use essa função.

def potencia(a, b):

    if b == 0:
        return 1

    resultado = a * potencia(a, b - 1)

    return resultado

numero = int(input("Digite o número: "))
expoente = int(input("Digite o expoênte: "))

print(f"A potência de {numero} por {expoente} é: {potencia(numero, expoente)}")

# 4°) Implemente uma função recursiva que calcule a somaS(n) onde o resultado é: Resposta = 1/1+1/2+1/3+1/4+...+1/n. Crie um programa que use essa função.
