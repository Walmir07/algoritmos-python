pares = []
impares = []

for i in range(15):

    valor = int(input())
    
    if valor % 2 == 0:
        pares.append(valor)
        if(len(pares) == 5):
            for j in range(5):
                print(f"par[{j}] = {pares[j]}")

            pares.clear()
            
    if valor % 2 != 0:
        impares.append(valor)
        if(len(impares) == 5):
            for k in range(5):
                print(f"impar[{k}] = {impares[k]}")

            impares.clear()

    if i == 14:
        if len(impares) != 0:
            for s in range(0, len(impares)):
                print(f"impar[{s}] = {impares[s]}")
                    
        if len(pares) != 0:
            for r in range(0, len(pares)):
                print(f"par[{r}] = {pares[r]}")


            