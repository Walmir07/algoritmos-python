# Quadrado e ao cubo

linhas = int(input())

for i in range(1, linhas + 1):

    j = i * i
    k = j * i

    print("{:.0f} {:.0f} {:.0f}".format(i, j, k))

    