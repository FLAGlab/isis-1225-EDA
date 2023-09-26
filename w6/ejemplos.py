## Raíz cuadrada
def sqrt(n):
    """
    calcúla la raiz cuadrada de n siguiendo el método de newton
    """
    def good_enough(guess, x):
        """
        Retorna si la raíz es lo suficientemente cercana al valor x
        """
        return abs(guess*guess - x) < 0.001
    def improve(guess, x):
        """
        Nuevo valor propuesto para la raíz cuadrada
        """
        return  (guess + (x/guess))/2
    def sqrt_iter(guess, x):
        if good_enough(guess, x):
            return guess
        else:
            sqrt_iter(improve(guess, x), x)
    sqrt_iter(1, n)

    



    
