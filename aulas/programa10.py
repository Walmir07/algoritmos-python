# Programa da aula 06/11/2025

# Revisão de listas:

#lista1 = ["VACA 1", "VACA2", "VACA 3"]
#lista2 = [1, 2, 3, 4, 5]

# Obter o maior valor:
#print()

################## Exercícios ##################

#Exercício 1: Crie uma lista a partir de 10 números obtidos de uma entrada e imprima o maior, o menor, a soma e a quantidade de elementos dessa lista. 

lista = []

for i in range(10):
    lista.append(int(input()))

print(f"O maior é: {max(lista)}")
print(f"O menor é: {min(lista)}")
print(f"A soma de todos é: {sum(lista)}")
print(f"A quantidade de elmentos é: {len(lista)}")

# Desafio 2: Crie uma lista de números obtidos de uma entrada que pedirá um novo número até que o número digitado seja 0 e imprima o maior, o menor, a soma e a quantidade de elementos dessa lista. 

lista = []

while True:

    numero = int(input("Digite o número: "))

    if numero == 0:
        break

    lista.append(numero)

print(f"O maior é: {max(lista)}")
print(f"O menor é: {min(lista)}")
print(f"A soma de todos é: {sum(lista)}")
print(f"A quantidade de números digitados: {len(lista)}")
