"""
# Desafio de pontos do dia 16/10/2025:

while True:
    sexo = input("Digite o sexo: M, F ou O: ")
    idade = int(input("Digite a sua idade: "))

    if sexo == "F" and idade >= 18:
        mulheres += 1

    if mulheres == 5:
        break

print(f"Entraram {mulheres} mulheres")

# Correção com o mesmo resultado:

mulheres = 0

while mulheres < 5:
    sexo = input("Digite o sexo: M, F ou O: ")
    idade = int(input("Digite a sua idade: "))

    if sexo == "F" and idade >= 18:
        mulheres += 1

print(f"Entraram {mulheres} mulheres")
"""
