def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

def fact(n):
    def fact_iter(n, res=1):
        if n == 0:
            return res
        else:
            return fact_iter(n-1, n*res)
    return fact_iter(n,1)











def factorial(n):
    """ Args: n entero, n >= 0 """
    if n == 0:  # caso especial
       return 1
    else:         # caso general
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact 


print(factorial(1000))
#print(factorial_rec(6))
print(fact(1000))

