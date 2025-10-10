#Exercício da aula: 10/10/2025

# Peça o nome e três notas de um aluno e posteriormente calcule a sua média e imprima juntamente com o seu nome, faça isso para 10 alunos:

for num in range(10):
    aluno = input("Digite o nome de um aluno: ")
    nota1 = float(input("Digite primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))

    media = (nota1 + nota2 + nota3)/3

    print(f"A média do {aluno} é: {media:.1f}")