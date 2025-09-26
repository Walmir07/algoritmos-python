import math

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - 4*a*c
print(delta)

if delta >= 0 and a != 0:
    r1 = (-b + math.sqrt(delta)) / (2*a)
    print("R1 = {:.5f}".format(r1))

    r2 = (-b - math.sqrt(delta)) / (2*a)
    print("R2 = {:.5f}".format(r2))
else:
    print("Impossivel calcular")
