#Programas da aula 25/09/2025

#Estilo de saída de dados:

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

print(f"Primeiro número: {numero1}, segundo número: {numero2}, terceiro número: {numero3}") #Formato inteiro

print("Primeiro número: {:.1f}, segundo número: {:.1f}, terceiro número: {:.1f}".format(numero1, numero2, numero3)) #Formato decimal

#Condicionais:

idade = 17

if idade < 18:
    print("É menor de idade")
else:
    print("Pode entrar")

#Verificação de idades:

"""
Morreu > 105
Quase lá [95, 104]
Anciã [80, 94]
Idosa [65, 79]
Adulto velho [50, 64]
Adulto [30, 49]
Jovem adulto [21, 29]
Jovem [18, 20]
Adolescentes [13, 17]
Criança [5, 12]
Bebê [0, 4]
Encomendando < 0
"""

idade = int(input("Digite a idade para obter a descrição: "))

if idade >= 105:
    print("Morreu")
elif idade > 95 and idade < 104:
    print("Quase lá")
elif idade > 80 and idade < 94:
    print("Anciã")
elif idade > 65 and idade < 79:
    print("Idosa")
elif idade > 50 and idade < 64:
    print("Adulto velho")
elif idade > 30 and idade < 49:
    print("Adulto")
elif idade > 21 and idade < 29:
    print("Jovem adulto")
elif idade > 18 and idade < 20:
    print("Jovem")
elif idade > 13 and idade < 17:
    print("Adolescente")
elif idade > 5 and idade < 12:
    print("Criança")
elif idade > 0 and idade < 4:
    print("Bebê")
else:
    print("Encomendando")

#Exercícios de pontos extra:

#Exercício 2:

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

if valor1 > valor2:
    print("O primeiro número é o maior")
else:
    print("O segundo número é o maior")

#Exercício 3:

primeiroValor = int(input("Primeiro valor: "))
segundoValor = int(input("Segundo valor: "))
terceiroValor = int(input("Terceiro valor: "))

if primeiroValor > segundoValor and primeiroValor > terceiroValor:
    print("O primeiro número é o maior")
elif segundoValor > primeiroValor and segundoValor > terceiroValor:
    print("O segundo número é o maior")
elif terceiroValor > primeiroValor and terceiroValor > segundoValor:
    print("O terceiro número é o maior")

#Exercicio 4:

val1 = int(input("Numero 1: "))
val2 = int(input("Numero 2: "))
val3 = int(input("Numero 3: "))
val4 = int(input("Numero 4: "))
val5 = int(input("Numero 5: "))

if val1 > val2 and val1 > val3 and val1 > val4 and val1 > val5:
    print("O primeiro número é o maior")
elif val2 > val1 and val2 > val3 and val2 > val4 and val2 > val5:
    print("O segundo número é o maior")
elif val3 > val1 and val3 > val2 and val3 > val4 and val3 > val5:
    print("O terceiro número é o maior")
elif val4 > val1 and val4 > val2 and val4 > val3 and val4 > val5:
    print("O quarto número é o maior")
elif val5 > val1 and val5 > val2 and val5 > val3 and val5 > val4:
    print("O quinto número é o maior")
