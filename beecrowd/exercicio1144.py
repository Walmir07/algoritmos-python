# Sequência lógica

linhas = int(input())

for i in range(1, linhas + 1):

    j = i * i
    k = j * i

    for m in range(2):
        print("{:.0f} {:.0f} {:.0f}".format(i, j, k))
        j += 1
        k += 1