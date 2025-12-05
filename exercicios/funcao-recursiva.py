#Exemplo de função recursiva - fatorial:

def fatorial(n):
  #Caso base: Parada da função
  if n == 1:
    return 1
  #Caso recursivo: A função chama a si mesmo
  else:
    return n * fatorial(n-1)

print(fatorial(5))
