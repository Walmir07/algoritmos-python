participantes = int(input())
lista = []
brindes = 0

for i in range(participantes):

    if len(lista) == 0:
        lista.append("F A C E")

    letras = input()
    
    letrasInver = lista[-1][::-1]

    if letras == letrasInver:
        brindes += 1
        lista.pop()
    else:  
        lista.append(letras)
    
print(brindes)



