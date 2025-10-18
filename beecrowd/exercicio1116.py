# Dividindo x por y

casos = int(input())

for i in range(casos):

    x, y = input().split()

    x = int(x)
    y = int(y)

    if y != 0:
        divisao = x / y
        print("{:.1f}".format(divisao))
    else:
        print("divisao impossivel")