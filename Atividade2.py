def calcular_fatorial(n): 
    if n < 0:
        raise ValueError("Número inválido! O fatorial não é definido para números negativos.")

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(calcular_fatorial(5))

