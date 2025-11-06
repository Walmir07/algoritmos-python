#Calculo de médias em Python: Aula 02/10/2025

nota1 = float(input("Digite a nota 1: ")) # Peso 30%
nota2 = float(input("Digite a nota 2: ")) # Peso 50%
nota3 = float(input("Digite a nota 3: ")) # Peso 20%

peso1 = 0.3
peso2 = 0.5
peso3 = 0.2

mediaAritmetica = (nota1+nota2+nota3) / 3
mediaPonderada = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)

print(mediaAritmetica)
print(mediaPonderada)

#Média aritmética de várias notas:

v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = 1, 1, 2, 2, 2, 3, 4, 5, 5, 9
p1, p2, p3, p4, p5, p9 = 2, 3, 1, 1, 2, 1

medAritmetica = (v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10) / 10
print("Média aritmética:", medAritmetica)

#medAritmetica = (v1*p1 + v2*p2 + v3*p3 + v4*p4 + v5) / 10

medPonderada = (1*2 + 2*3 + 3*1 + 4*1 + 5*2 + 9*1) /(p1+p2+p3+p4+p5+p9)


#Médias de salários:
 
salario1 = 12890.78 # 3 pessoas
salario2 = 5800.50  # 7 pessoas
salario3 = 13000.00 # 4 pessoas

mediaAritmetica = (salario1 + salario2 + salario3) / 3
print("A média aritmética dos salários é: {:.2f}".format(mediaAritmetica))

mediaPonderada = (salario1 * 3 + salario2 * 7 + salario3 * 4) / (3 + 7 + 4)
print("A média ponderada dos salários é: {:.2f}".format(mediaPonderada))

#Exercicio

# Valendo ponto: 10

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

peso1 = n1 * 0.3
peso2 = n2 * 0.3
peso3 = n3 * 0.2
peso4 = n4 * 0.2

ponderada = (n1*peso1 + n2*peso2 + n3*peso3 + n4*peso4) / (peso1+peso2+peso3+peso4)

if ponderada >= 7:
    print("Aprovado")
elif ponderada >= 5 and ponderada < 7:
    print("Recuperação")
else:
    print("Reprovado")