# Intervalo 2

n = int(input())
numberIn = 0
numberOut = 0

for i in range(n):

    x = int(input())

    if x >= 10 and x <= 100:
        numberIn += 1
    else:
        numberOut += 1

print("{:.0f} in".format(numberIn))
print("{:.0f} out".format(numberOut))