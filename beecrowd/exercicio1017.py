tempoGasto = int(input())
velocidadeMedia = int(input())

distanciaPercorrida = tempoGasto * velocidadeMedia

combustivelGasto = distanciaPercorrida / 12

print("{:.3f}".format(combustivelGasto))