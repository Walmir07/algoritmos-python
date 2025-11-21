# Programa da aula 21/11/2025

# Função

# Exemplo 1 - Função para juntar textos:

def juntar(x, y):
    resposta = x + y
    return resposta

entrada1 = input("Digite algo: ")
entrada2 = input("Digite outra coisa: ")

res = juntar(entrada1, entrada2)

print(res)

#Exemplo 2 - Função para verificar maior que 10:

def maiorQue10(x):
    if x > 10:
        return True
    else:
        return False
    
#Testando 10 vezes
for i in range(10): #Testando 10 vezes
    valor = int(input("Digite o valor: "))
    print(maiorQue10(valor))

#Exemplo 3 - Função para soma:

def soma(x, y):
    res=  x + y
    return res

def multiplicar(x, y):
    res=  x * y
    return res

numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite um valor: "))

print("A soma é: ", soma(numero1, numero2))
print("A multiplicação é: ", multiplicar(numero1, numero2))

elem1 = int(input("Digite o valor 1: "))
elem2 = int(input("Digite o valor 2: "))
elem3 = int(input("Digite o valor 3: "))
elem4 = int(input("Digite o valor 4: "))

resp1 = soma(elem1, elem2)
resp2 = soma(elem3, elem4)
print(resp1)
print(resp2)

resposta = multiplicar(resp1, resp2)
print(resposta)