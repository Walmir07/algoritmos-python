# Seleção em vetor I

a = []

for i in range(100):
    a.append(float(input()))

    if a[i] <= 10:
        print("A[{:.0f}] = {:.1f}".format(i, a[i]))
