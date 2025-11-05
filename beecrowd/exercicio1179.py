pares = []
impares = []

for i in range(0, 15):
    valor = int(input())
    
    if valor / 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
    for j in range(5):
        print(f"par[{j}] = {pares[j]}")
    
    for r in range(5):
        print(f"impar[{r}] = {impares[r]}")
    
    if len(pares) == 5:
        pares.clear()
        
    if len(impares) == 5:
        impares.clear()
    