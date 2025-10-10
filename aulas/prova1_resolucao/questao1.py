# 1 - João quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem... (Continua)

distancia = float(input("Digite a distância: "))
litrosNecessarios = distancia / 12

print("Serão necessários {:.2f} litros para fazer a viagem".format(litrosNecessarios))

# 2 - Faça um programa que que pergunte o turno que você estuda... (Continua)

turno = input("Digite o turno: (M, V ou N), onde M - Matutino, V - Vespertino e N - Noturno: ")

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")

# 3 - Joana fez a lista de exercícios e a mini-prova... (Continua)

notaLista = float(input("Digite a nota da lista"))
notaMiniprova = float(input("Digite a nota da mini-prova"))

mediaPonderada = (notaLista * 0.2) + (notaMiniprova * 0.8)

print("A média ponderada de Joana é {:.2f}".format(mediaPonderada))

# 4 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica... (Continua)

consumo = float(input("Digite o valor do consumo"))
tipo = input("Digite a categoria: R para residencial, C para comercial e I para Industrial: ")
conta = 0

if tipo == "R":
    if consumo <= 500:
        conta = consumo * 0.40
    elif consumo > 500:
        conta = consumo * 0.65
elif tipo == "C":
    if consumo <= 1000:
        conta = consumo * 0.60
    elif consumo > 1000:
        conta = consumo * 0.70
elif tipo == "I":
    if consumo <= 5000:
        conta = consumo * 0.50
    elif consumo > 5000:
        conta = consumo * 0.60

print("O consumo foi de: R$ {:.2f}".format(conta))