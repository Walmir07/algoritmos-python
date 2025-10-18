# Soma de Ímpares Consecutivos II

n = int(input())

for i in range(n):

    soma = 0

    x, y = input().split()

    x = int(x)
    y = int(y)

    if x > y:
        x, y = y, x

    for j in range(x + 1, y):

        if j % 2 != 0:
            soma += j 

    print(soma)