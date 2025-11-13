# Programa da aula 06/11/2025

# Estrutura de dados - Tupla: Lista imutável.

tuplaNumeros = (1, 2, 3, 4, 5)

# Estrutura de dados - Dicionário: Possui chave e valor.

pessoa = {"nome": "Alvaro", "idade": 21, "CPF": "123.456.789-00"}

print("NOME = ", pessoa["nome"])
print("IDADE = ", pessoa["idade"])
print("CPF = ", pessoa["CPF"])

#Atividade da aula:

#nome, matrícula, cpf, nota1, nota2, nota3, nota4

print("")

alunos = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    cpf = input("Digite o cpf do aluno: ")
    nota1 = float(input("Digite a nota 1 do aluno: "))
    nota2 = float(input("Digite a nota 2 do aluno: "))
    nota3 = float(input("Digite a nota 3 do aluno: "))
    nota4 = float(input("Digite a nota 4 do aluno: "))

    print("")
    dicionario = {"nome": nome, "matricula": matricula, "cpf": cpf, "nota1": nota1, "nota2": nota2, "nota3": nota3, "nota4": nota4,}
    alunos.append(dicionario)

#Imprime todas as informações dos alunos:
print("Informações de todos os alunos: \n")
for aluno in alunos:
    print(aluno)

#Imprime apenas alunos com a nota 2 maior que 70:
print("\n Alunos com nota acima de 70: \n")
for aluno in alunos:
    if aluno["nota2"] > 70:
        print(aluno)

#Imprime o nome do aluno + a média final:
print("\n Nome do aluno + sua média final: \n")
for aluno in alunos:
    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"] + aluno["nota4"]) / 4
    print(f"{aluno["nome"]} - {media}")


