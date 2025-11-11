casos = int(input())

for i in range(casos):
    
    quantNotas = int(input())
    nota = input().split()
    notas = []
    
    for j in range(quantNotas):
        notas.append(int(nota[j]))
        
    ordem = sorted(notas, reverse=True)
    certos = 0
     
    for k in range(quantNotas):
    
        if notas[k] == ordem[k]:
            certos += 1
        
    print(certos)