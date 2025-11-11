n, k = input().split(" ")

n = int(n)
k = int(k)

alunos = []

for i in range(n):
    aluno = input()
    alunos.append(aluno)
    
    alunos.sort()
    
print(alunos[k - 1])