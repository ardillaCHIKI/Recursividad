def factorial(n):
    if n == 0:
        print(f"factorial(0) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {result}")
        return result

print(factorial(5))  # Cambia 5 por el número que desees calcular