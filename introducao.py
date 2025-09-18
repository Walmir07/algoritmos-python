#Conceitos e testes iniciais de introdução ao python:

x = 3
y = 5
valor = x+y
print(x)
print(y)
print(valor)
texto = "Meu texto"
print(texto)
nome = input("Digite seu nome: ")
print("Seu nome é: " + nome)

#Exemplo de comparações:

comparacao1 = x > y
print(comparacao1)

comparacao2 = y > x;
print(comparacao2)

print("Texto 1","Texto 2")

#Exemplo de média:

nota1 = 8.0
nota2 = 10.0
media = (nota1 + nota2)/2
print("Primeira nota:", nota1)
print("Segunda nota:", nota2)
print("Média:", media)

#Exemplo sobre maça:

quantMaca = 5
valorMaca = 4.5
total = quantMaca * valorMaca
print("Comprei", quantMaca, "maças por R$", valorMaca, "cada. Que deu um total de R$", total, "ao todo.")

#Exemplo com input e entradas:

nome = "Walmir"
print("Bom dia,", nome)
entrada = input("Digite o seu nome:")
print("Bom dia,", entrada)

#Calculo de médias com input:

primeiraNota = float(input("Digite a primeira nota:"))
segundaNota = float(input("Digite a primeira nota:"))
mediaFinal = (primeiraNota + segundaNota)/2;
print("Primeira nota:", primeiraNota, ". Segunda nota:", segundaNota, ". Sua média é:", mediaFinal)