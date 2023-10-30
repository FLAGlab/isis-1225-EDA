def factorial(n):
    """ Args: n entero, n >= 0 """
    def iter(n, accumulator):
        """ Args: n entero, n >= 0
                  acumulator entero, 1 <= accumulator <= n! """
        if n == 0:
            return accumulator
        else:
            return iter(n-1, accumulator*n)
    return iter(n, 1)


print(factorial(6))