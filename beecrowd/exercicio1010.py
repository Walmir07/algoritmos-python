#Questão 1010 - Cálculo simples

codigoPeca1, numeroPeca1, valorPeca1 = input().split() 

codigoPeca1 = int(codigoPeca1)
numeroPeca1 = int(numeroPeca1)
valorPeca1 = float(valorPeca1)

codigoPeca2, numeroPeca2, valorPeca2 = input().split() 

codigoPeca2 = int(codigoPeca2)
numeroPeca2 = int(numeroPeca2)
valorPeca2 = float(valorPeca2)

valorPagar = (numeroPeca1 * valorPeca1) + (numeroPeca2 * valorPeca2)

print("VALOR A PAGAR: R$ {:.2f}".format(valorPagar))