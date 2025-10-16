# Aula 16/10/2025 - Revisão sobre estruturas de repetição


########## Revisão do for ##########


# Exemplo de loop for:

for num in range(100):
    print("Mande flores para a sua namorada")

# Exemplo de for com 1 parâmetro:

for i in range(10):
    numero = int(input("Digite o número {:.0f}: ".format(i)))
    print(numero) # Irá repetir 10 vezes

# Exemplo de for com 2 parâmetros:

for i in range(1, 10):
    numero = int(input("Digite o número {:.0f}: ".format(i)))
    print(numero) # Limita a repetição iniciando de 1 até o 9

# Exemplo de for com 3 parâmetros:

for i in range(1, 10, 2):
    numero = int(input("Digite o número {:.0f}: ".format(i)))
    print(numero) # Limita a repetição iniciando de 1 até o 9 incrementando de 2 em 2

# Exemplo de for crescente:

for i in range(0, 103, 3):
    print("Número = ", i)

# Exemplo de for decrescente:

for i in range(103, 0, -3):
    print("Número = ", i)

# Número maior com loop for:

maior = float("-inf")

for i in range(5):
    numero = int(input("Digite um número:"))
    if numero > maior:
        maior = numero

print(f"O maior é {maior}")

# Recebendo um número em minutos e fazendo a sua contagem regressiva em segundos:

import time

minutos = int(input())

segundos = minutos * 60

for num in range(segundos, -1, -1):
    print(f"Faltam: {num} segundos")
    time.sleep(5)


########## Revisão do while ##########


# Digitando um número enquanto ele for diferente de -1 utilizando while:

numero = 0

while numero != -1:
    numero = int(input("Digite um número"))