# Preenchimento de Vetor III

valor = float(input())
lista = []

for i in range(100):
    
    lista.append(valor)
    
    print(f"N[{i}] = {valor:.4f}")
    
    valor /= 2