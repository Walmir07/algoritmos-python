valor = int(input())

print(valor)

nota100 = valor // 100
valor = valor % 100
print(nota100, "nota(s) de R$ 100,00")

nota50 = valor // 50
valor %= 50
print(nota50, "nota(s) de R$ 50,00")

nota20 = valor // 20
valor %= 20
print(nota20, "nota(s) de R$ 20,00")

nota10 = valor // 10
valor %= 10
print(nota10, "nota(s) de R$ 10,00")

nota5 = valor // 5
valor %= 5
print(nota5, "nota(s) de R$ 5,00")

nota2 = valor // 2
valor %= 2
print(nota2, "nota(s) de R$ 2,00")

nota1 = valor // 1
valor %= 1
print(nota1, "nota(s) de R$ 1,00")