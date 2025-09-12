#Faça um programa que calcule a área e o perímetro de um retângulo recebendo a base e a altura:

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area = base * altura
print("A área do retângulo é:", area)

perimetro = base + base + altura + altura
print("O perímetro do retângulo é:", perimetro)