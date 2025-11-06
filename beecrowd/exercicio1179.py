pares = []
impares = []

for i in range(10):

    valor = int(input())
    
    if valor / 2 == 0:
        pares.append(valor)
        if(len(pares) == 5):
            for j in range(5):
                print(f"par[{j}] = {pares[j]}")

            pares.clear()
    else:
        impares.append(valor)
        if(len(impares) == 5):
            for k in range(5):
                print(f"impar[{k}] = {impares[k]}")

            pares.clear()
    