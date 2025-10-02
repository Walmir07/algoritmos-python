#Exercícios da aula: 02/10/2025

#Qual o número maior:

numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
numero3 = int(input("Digite o número 3: "))

if numero1 == numero2 == numero3:
    print("Todos os números são iguais")
elif (numero1 == numero2 and numero1 > numero3) or (numero1 == numero3 and numero1 > numero2) or (numero2 == numero3 and numero2 > numero1):
    print("Não existe maior")
elif numero1 > numero2 and numero1 > numero3:
    print("O primeiro valor é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print("O segundo valor é o maior")
elif numero3 > numero1 and numero3 > numero2:
    print("O terceiro valor é o maior")

#Melhor resposta:

numero1 = int(input("Digite o número 1: ")) #3
numero2 = int(input("Digite o número 2: ")) #5
numero3 = int(input("Digite o número 3: ")) #9
numero4 = int(input("Digite o número 4: ")) #7
numero5 = int(input("Digite o número 5: ")) #1

maior = numero1

if numero2 >= maior:
    maior = numero2

if numero3 >= maior:
    maior = numero3

if numero4 >= maior:
    maior = numero4 

if numero5 >= maior:
    maior = numero5

print("Maior: ", maior)

#Converter número em string na saída:

n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
n3 = int(input("Digite o número 3: "))
n4 = int(input("Digite o número 4: "))
n5 = int(input("Digite o número 5: "))

print(numero1+numero2+numero3+numero4+numero5) #Soma

print(str(n1) + str(n2) + str(n1) + str(n1) + str(n1)) #Concatenação
print("{}{}{}{}{}".format(n1, n2, n3, n4, n5))
print(f"{n1}{n2}{n3}{n4}{n5}")
print(n1,n2,n3,n4,n5)

#IF ternário

idade = 18
maiorDeIdade = "Sim" if idade >= 18 else "Não"






