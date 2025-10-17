# Experiências

quantia = int(input())

coelhos = 0
ratos = 0
sapos = 0
total = 0
  
for i in range(1, quantia + 1):

    quantCobaias, tipo = input().split()
    quantCobaias = int(quantCobaias)

    total += quantCobaias

    if tipo == "C":
        coelhos += quantCobaias
    elif tipo == "R":
        ratos += quantCobaias
    elif tipo == "S":
        sapos += quantCobaias

percentualCoelhos = (coelhos * 100) / total
percentualRatos = (ratos * 100) / total
percentualSapos = (sapos * 100) / total

print("Total: {:.0f} cobaias".format(total))
print("Total de coelhos: {:.0f}".format(coelhos))
print("Total de ratos: {:.0f}".format(ratos))
print("Total de sapos: {:.0f}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format(percentualCoelhos))
print("Percentual de ratos: {:.2f} %".format(percentualRatos))
print("Percentual de sapos: {:.2f} %".format(percentualSapos))

