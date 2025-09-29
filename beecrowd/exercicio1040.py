n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / (2+3+4+1)
print("Media: {:.1f}".format(media))

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: {:.1f}".format(notaExame))
    media = (media + notaExame) / 2
    if media >= 5:
        print("Aluno aprovado.")
    if media <= 4.9:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media))
