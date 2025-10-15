# Soma de números consecutivos I

x = int(input())
y = int(input())

soma = 0

if x < y:
    while x < y:
        if x % 2 != 0:
            soma += x
        x += 1
else:
    while y < x:
        if y % 2 != 0:
            soma += y
        y += 1

print("{:.0f}".format(soma))
