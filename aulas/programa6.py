# Conceitos e programas da aula 10/10/2025:

# Laço de repetição FOR:

"""
for num in range(1, 11):
    print(num) # Imprime de 1 a  10
"""

########## Exemplos ##########

# Exemplo de laço for com soma:

"""
resultado = 0

for num in range(1, 6):
    resultado += num
    print(resultado)

# Faça um algoritmo que mostre os números inteiros de 1 a 30:

for num in range(1, 31):
    print(num)

# Faça um algoritmo que faça a soma de todos os números pares de 1 a 20:

soma = 0

for num in range(2, 21, 2):
    soma += num
    
print(soma)

# Soma de 10 números inteiros obtidos a partir de 10 entradas:

resultado = 0

for num in range(1, 11):
    entrada = int(input("Digite um valor: "))
    resultado = resultado + entrada

print(resultado)

"""
"""
# Receba 10 entradas numéricas e imprima qual dos números é maior:

maior = 0

for num in range(1, 11):
    numero = int(input("Digite o número: "))
    if numero > maior:
        maior = numero

print("O maior número é: {:.0f}".format(maior))

# Fazendo o mesmo sistema usando listas

numeros = input("Digite o número: ")
maior = 0

elementos = numeros.split(" ")

for num in range(10):

    numero = int(elementos[num])

    if numero > maior:
        maior = numero

print("O maior número é: {:.0f}".format(maior))
"""

# Laço de repetição WHILE:

entrada = int(input("Digite um valor: "))

while entrada > 0:
    print(entrada)
    entrada -= 1

# Imprimir até o valor da entrada:

entrada = int(input("Digite o número que quer chegar: "))
valor = 1

while valor <= entrada:
    print(valor)
    valor += 1

# Repetir o input até o zero ser digitado no terminal:

numero = int(input("Digite um valor: "))

while numero > 0:
    print(numero * 2)
    numero = int(input("Digite um número: "))



