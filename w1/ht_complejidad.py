def darElementoEnPosicion(lista, pos): 
    """ Problema 1.
    Retornar el elemento en una posición (positiva) de una lista. El primer elemento esta en la posicion 0.
    Resultado: elemento en la posicion. None si posición inválida. """
    if 0 <= pos and pos < len(lista): 
        return lista[pos]
    else:
        return None
    
# Calcular la cantidad de veces que se repite la instrucción    
# Comparaciones <= :
# Comparaciones < :
# Operador and :
# Operador [] :
# Instrucción return : 

# Calcular el orden de crecimiento temporal del algoritmo:



def busquedaSecuencialNativo(lista, elemento): 
    """ Problema 2.
    Busqueda Secuencial/Lineal de un elemento en una lista (recorrido nativo) Resultado: Indice en la 
    lista donde se encuentra el elemento. -1 si no se encuentra. """
    i= 0
    pos = -1
    for item in lista:
        if item == elemento: 
            pos = i
            break 
        else:
            i += 1 
    return pos

# Calcular la cantidad de veces que se repite la instrucción    
# Asignación :
# Incremento :
# Comparación :
# Operador in :

# Calcular el orden de crecimiento temporal del algoritmo:



def busquedaMatriz(matriz, filas, columnas, elemento): 
    """ Problema 3.
    Busqueda de un elemento al recorrer una matriz de filas x columnas elementos Resultado: 
    (fila, columna) donde se encuentra el elemento. (-1, -1) si no se encuentra. """
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == elemento:
                return f, c 
    return -1, -1

# Calcular la cantidad de veces que se repite la instrucción    
# Asignación :
# Incremento :
# Comparación :
# Operador in :
# Operador [] :

# Calcular el orden de crecimiento temporal del algoritmo:


def contarMayoresMenores(lista, elemento):
    """ Problema 4.
    Contar el total de elementos mayores y de elementos menores a un elemento dado. Resultado: 
    total de elementos mayores y total de elementos menores a un elemento """
    mayores = 0
    menores = 0
    for item in lista:
        if item > elemento: 
            mayores += 1
        if item < elemento: 
            menores += 1
    return mayores, menores

# Calcular la cantidad de veces que se repite la instrucción    
# Asignación :
# Incremento :
# Comparación > :
# Comparación < :
# Operador in :

# Calcular el orden de crecimiento temporal del algoritmo:


def contarTripletasSumaCero(lista): 
    """ Problema 5.
    Contar 3-tuplas <e1, e2, e3> de elementos en la lista tal que e1 + e2 + e3 sea igual a 0 Resultado: 
    total de 3-tuplas de elementos cuya suma es 0 """
    contador = 0
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            for k in range(j+1, len(lista)):
                if lista[i]+lista[j]+lista[k] == 0:
                    contador += 1 
    return contador

# Calcular la cantidad de veces que se repite la instrucción    
# Asignación :
# Incremento :
# Comparación :
# Operador in :

# Calcular el orden de crecimiento temporal del algoritmo:


def incognita(n): 
    """ Problema 6. v1
    Entender el algoritmo y decir que problema resuelve """
    sum = 0
    while n > 0: 
        sum += n 
        n = n // 2 
    return sum

def incognita(n): 
    """ Problema 6. v2
    Entender el algoritmo y decir que problema resuelve """
    sum = 0
    while n > 0:
        for i in range(n): 
            sum += 1
        n = n // 2 
    return sum

# Calcular la cantidad de veces que se repite la instrucción    
# Asignación :
# Incremento :
# Comparación :
# Operador in :

# Calcular el orden de crecimiento temporal del algoritmo:
# Qué algoritmo es más eficiente? :








               
    





