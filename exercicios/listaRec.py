def restoDivisaoSucessiva(a, b):

    if a < b:
        return 0
   
    return 1 + restoDivisaoSucessiva( a - b, b)

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

print(f"A divisão por subtrações de {dividendo} por {divisor} é: {restoDivisaoSucessiva(dividendo, divisor)}")