t = int(input())
lista = []

for i in range(0, 1000):
    
    for j in range(0, t):
        
        lista.append(j)
        
    print(f"N[{i}] = {lista[i]}")