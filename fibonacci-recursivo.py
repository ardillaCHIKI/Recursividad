def fibonacci_recursivo(n):
    print(f"Llamando a fibonacci_recursivo({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Ejemplo de uso
if __name__ == "__main__":
    numero = 6  # Cambia este número para probar con otros valores
    resultado = fibonacci_recursivo(numero)
    print(f"El resultado de fibonacci_recursivo({numero}) es {resultado}")