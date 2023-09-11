def factorial(n):
    """ Args: n entero, n >= 0 """
    if n == 0:  # caso especial
       return 1
    else:         # caso general
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact 


print(factorial(6))