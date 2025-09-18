#Crie um programa para um supermercado que guarda dados importantes.

valorArroz = 4.50
valorFeijao = 5.0
valorMacarrao = 5.0
valorOleo = 8.00

produto = int(input("Qual produto você deseja comprar? 1: Arroz | 2: Feijão | 3: Macarrão | 4: Oleo: "))

quantidade = int(input("Quantidade de produtos: "))

if produto == 1:
    total = valorArroz * quantidade
elif produto == 2:
    total = valorFeijao * quantidade
elif produto == 3:
    total = valorMacarrao * quantidade
elif produto == 4:
    total = valorOleo * quantidade

print("O preço total é R$ ", total)