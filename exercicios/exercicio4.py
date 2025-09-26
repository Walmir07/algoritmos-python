#Número maior ou igual:

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

if numero1 > numero2:
    print(numero1, "é o maior")
elif numero2 > numero1:
    print(numero2, "é o maior")
else:
    print("Os números são iguais")


numero1 = int(input("Digite o primeiro valor: "))

if numero1 > 0:
    print(numero1, "é positivo")
elif numero1 < 0:
    print(numero1, "é positivo")
else:
    print("O número é neutro")