def calcular_fatorial(n):
    if n < 0:
        raise Exception("Número inválido!")

    resultado = 1
    if n == 0:
        resultado = 1
    else:
        for i in range(1, n + 1):
            resultado *= i
    return resultado

print(calcular_fatorial(5))
