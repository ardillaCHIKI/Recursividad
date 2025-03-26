def fibonacci_iterativo(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Ejemplo de uso
if __name__ == "__main__":
    numero = int(input("Introduce un número: "))
    resultado = fibonacci_iterativo(numero)
    print(f"El Fibonacci de {numero} es {resultado}")