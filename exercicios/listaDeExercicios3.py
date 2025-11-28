# 1°) Escreva uma função que recebe dois números inteiros como parâmetro e retorna o produto deles. Depois crie os parâmetros e chame a função.

def produto(a, b):
    return b * a

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = produto(num1, num2)

print(f"O produto é: {resultado}")

# 2°) Escreva uma função que recebe dois números inteiros como parâmetro e retorna o maior deles. Depois crie os parâmetros e chame a função.

def maior(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = maior(num1, num2)

print(f"O maior dos números é: {resultado}")

# 3°) Escreva uma função que recebe uma letra como parâmetro e verifica se a letra digitada é vogal ou consoante, retornando as strings “vogal” e “consoante” conforme a avaliação. Depois utilize a função.

def tipoLetra(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return "vogal"
    else:
        return "consoante"

letra = input("Digite a letra: ")
letra = letra.lower()

resultado = tipoLetra(letra)

print(f"A letra escrita é: {resultado}")

# 4°) Escreva uma função que receba uma lista de inteiros como parâmetro e retorne a média de todos os itens da lista. Depois crie o parâmetro e chame a função.

def mediaLista(lista):
    media = sum(lista) / len(lista)
    return media

lista = [15, 15, 15]

resultado = mediaLista(lista)

print(f"A media da lista é: {resultado}")

# 5°) Escreva uma função que receba uma lista de inteiros como parâmetro e retorne o maior valor entre todos os itens da lista. Depois crie o parâmetro e chame a função.

def maiorLista(lista):

    for i in range(0, len(lista)):
        if i == 0:
            maior = lista[i]
        else:
            if lista[i] > maior:
                maior = lista[i]
    return maior

lista = [7, 2, 8, 55]

resultado = maiorLista(lista)

print(f"A maior da lista é: {resultado}")

# 6°) Escreva uma função que receba um número inteiro como parâmetro e retorne o seu fatorial. Depois crie o parâmetro e chame a função.

def fatorar(numero):
    fatoral = 1

    for i in range(1, numero + 1):
        fatoral *= i

    return fatoral

resultado = fatorar(5)

print(f"O fatoral do número é: {resultado}")

# 7°) Escreva uma função que receba um número inteiro do usuário como parâmetro (n) e retorne uma lista com os n primeiros números da sequência de Fibonacci.

def fibonacci(n):

    fib = [0, 1]

    for i in range(2, n):
        fib.insert(i, fib[-1] + fib[-2])

    return fib

numero = int(input("Digite o número de elementos: "))

resultado = fibonacci(numero)

print(f"Os {numero} primeiros elementos de fibonacci são: {resultado}")

# 8°) Escreva uma função que receba um número inteiro do usuário como parâmetro (n) e retorne um Boolean dizendo se ele é primo ou não.

def numeroPrimo(numero):

    if numero < 2:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

numero = int(input("Digite o número para verificar se é primo: "))

resultado = numeroPrimo(numero)

if resultado:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")