alunos = []
notas = []

for i in range(2):

    aluno = {"nome": input("Digite o nome de um aluno: "), "matricula": input("Digite a matrícula do aluno: "), "idade": int(input("Digite o a idade do aluno: ")), "CPF": input("Digite o cpf do aluno: "), "nota1": float(input("Digite a nota 1: ")), "nota2": float(input("Digite a nota 2: ")), "nota3": float(input("Digite a nota 3: ")), "nota4": float(input("Digite a nota 4: "))}

    alunos.append(aluno)

    print("_________________ Dados do aluno _________________\n")

    print(f"NOME = {aluno["nome"]}")
    print(f"MATRÍCULA = {aluno["matricula"]}")
    print(f"IDADE = {aluno['idade']}")
    print(f"CPF = {aluno['CPF']}")
    print(f"NOTA 1 = {aluno['nota1']}")
    print(f"NOTA 2 = {aluno['nota2']}")
    print(f"NOTA 3 = {aluno['nota3']}")
    print(f"NOTA 4 = {aluno['nota4']}")

print(f"\nLista de alunos cadastrados: \n") 
print(alunos)

for j in range(2):

    alunoAtual = alunos[j]

    soma = alunoAtual["nota1"] + alunoAtual["nota2"] + alunoAtual["nota3"] + alunoAtual["nota4"]

    media = soma / 4
    
    if alunoAtual["nota2"] >= 70:

        print("\n Alunos com segunda nota acima de 70: \n")

        acimaDe70 = [alunoAtual["nome"]]        

    print(f"\n########### Dados do aluno {alunoAtual["nome"]} ##########\n")

    nomeAlunoAtual = [alunoAtual["nome"]]
    mediaAlunoAtual = media


print(f"Nomes: {nomeAlunoAtual}")
print(f"Médias: {mediaAlunoAtual}")

for k in range(len(nomeAlunoAtual)):
    print(f"Nome aluno {k}: {nomeAlunoAtual[k]}")
    print(f"Média aluno {k}: {mediaAlunoAtual[k]}")
