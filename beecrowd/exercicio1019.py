segundos = int(input())

minutos = segundos // 60
segundos %= 60

horas = minutos // 60
minutos %= 60

print(f"{horas}:{minutos}:{segundos}")