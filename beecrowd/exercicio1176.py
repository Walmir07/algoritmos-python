#Fibonacci em vetor

tentativas = int(input())

fibonacci = [0, 1]

for i in range(2, 61):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

for i in range(tentativas):
    valor = int(input())
    print(f"Fib({valor}) = {fibonacci[valor]}")