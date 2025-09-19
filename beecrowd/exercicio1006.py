#Questão 1006 - Média 2

a = float(input())
b = float(input())
c = float(input())

pesoA = 2
pesoB = 3
pesoC = 5
somaPesos = pesoA + pesoB + pesoC

media = (a * pesoA + b * pesoB + c * pesoC) / somaPesos

print("MEDIA = {:.1f}".format(media))