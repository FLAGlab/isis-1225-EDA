def fibonacci_iter(n):
    """
    Versión iterativa del cálculo de los números de Fibonacci
    """
    if n == 0:    # caso base 1
        return 0
    elif n == 1: # caso base 2
        return 1
    else:   # caso iterativo
        bp = (1 + math.sqrt(5.0))/2.0
        bn = (1 - math.sqrt(5.0))/2.0
        pos = bp
        neg = bn
        for i in range(2, n+1):
            pos =  pos * bp
            neg =  neg * bn
        return (pos - neg)/math.sqrt(5.0)