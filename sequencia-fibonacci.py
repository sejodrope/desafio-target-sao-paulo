def pertence_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

numero = int(input("Digite um número para verificar: "))
if pertence_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")