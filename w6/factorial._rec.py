def factorial(n):
    """ Args: n entero, n >= 0 """
    if n == 0 or n == 1:
        # casos especial y base
        return 1
    else:   # caso recursivo
        fact = n * factorial(n-1)
        return fact


print(factorial(6))