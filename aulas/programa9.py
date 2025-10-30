# Programa da aula 30/10/2025

# Estrutura de dados - Fila:

# fila.remove("Magnum")  # remove: passa o item que quer remover
# fila.pop("0")          # pop: passa a posição do item que quer remover

fila = ["Magnum", "Pedro", "Zeca", "Pedro"]
#print(fila)

#FILA:

for i in range(len(fila)):
    proximaPessoa = fila[0]
    fila.pop(0)
    print(proximaPessoa)
    
print(fila)

pilha = ["Magnum", "Pedro", "Zeca", "Pedro"]
#print(pilha)

#PILHA:

for i in range(len(pilha)): 
    proximaPessoa = pilha[-1]
    pilha.pop(-1)
    print(proximaPessoa)
    
print(pilha)

#################### Práticas ###################

#Exercício 1:
#Quantas Goiabas estão na lista?

frutas = ["GOIABA", "MAÇA", "UVA", "BANANA", "LARANJA", "GOIABA", "UVA", "UVA"]

print(frutas.count("GOIABA"))       #count: Conta a quantidades de GOIABAS presentes na lista
print(frutas.count("UVA"))          #count: Conta a quantidades de UVAS presentes na lista
print(frutas.count("JABOTICABA"))   #count: Conta a quantidades de JABOTICABAS presentes na lista

posicaoDesejada = frutas.index("GOIABA") #index: Obtém o índice da GOIABA ou elemento desejado