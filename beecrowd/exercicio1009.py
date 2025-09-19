# Questão 1009 - Salário com bônus

nomeVendedor = str(input())
salarioFixo = float(input())
totalVendas = float(input())
comissao = totalVendas * 15 / 100

salarioTotal = salarioFixo + comissao

print("TOTAL = R$ {:.2f}".format(salarioTotal))