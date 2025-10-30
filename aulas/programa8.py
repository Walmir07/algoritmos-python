# Programa da aula 30/10/2025

# Estrutura de dados:

# Criação de lista a partir de uma string:

nomes = "Maria, Pedro, Joana, Eduarda"

lista = nomes.split(", ")

print(lista)

# Lista 1 - Arrays:

lista1 = [6, 8, 12, 1, 4, 5, 0, 10]
        # 0, 1, 2, 3, 4, 5, 6, 7 - Índices indo
    # -8, -7, -6, -5, -4, -3, -2, -1 - Índices voltando

print(lista1[0])  #Acessando o elemento do índice 0: 6
print(lista1[1])  #Acessando o elemento do índice 1: 8
print(lista1[-1]) #Acessando o elemento do índice -1: 10
print(lista1[-6]) #Acessando o elemento do índice -6: 12

# Exemplo de acesso:

info = [6, 12, True, 12, True, 4, 0, 5, 10800]

print(info[-1]) # Imprimindo salário de 10800

# Exemplo com métodos:

nomesFesta = []

for i in range(5):
    nome = input(f"Digite um nome {i+1}: ")
    nomesFesta.append(nome) # Append: Atribui um elemento no final da lista

nomesFesta.sort() # Sort: Ordena a lista em ordem crescente

print(nomesFesta)

# Adição de elementos com Append:

minhaLista = []

minhaLista.append("Maria")
minhaLista.append("João")
minhaLista.append("Pedro")
minhaLista.append("Lucas")

print(minhaLista)

# Utilizando FOR para listar:

for elemento in minhaLista: # Em listas, o for não necessita do range()
    print(elemento)

# Utilizando separador (sep) para listar:

print(*minhaLista, sep="\n")

# Programa que pede 20 números e apresenta o maior:

numeros = []

for i in range(20):
    numeros.append(int(input("Dgite um número: ")))

numeros.sort() # Possui também o método "reverse" para reverter a ordem dos números, com reverse=true

print(numeros[-1]) #Retorna o maior
print(numeros[0])  #Retorna o menor

print(*numeros, sep="\n") # Lista todos os números por linha

######################### Exercícios #########################

# Exercício 1:

# Crie um programa que lê 10 numeros e imprima em orde crescente e decrescente, utilizando listas:

minhaLista = []

for num in range(10):
    minhaLista.append(input("Digite um nome: "))

minhaLista.sort()

print(*minhaLista, sep="\n")

minhaLista.sort(reverse=True)

print(*minhaLista, sep="\n")