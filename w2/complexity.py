#### 1
def darElementoEnPosicion(lista, pos):
    """
    Retornar el elemento en una posición (positiva) de una lista. 
    El primer elemento esta en la posicion 0.
    Resultado: elemento en la posicion. None si posición inválida.
    """
    if 0 <= pos and pos < len(lista):
        return lista[pos]
    else:
        return None
    
#### 2
def busquedaSecuencialNativo(lista, elemento):
    """
    Busqueda Secuencial/Lineal de un elemento en una lista (recorrido nativo)
    Resultado: Indice en la lista donde se encuentra el elemento. -1 si no se encuentra.
    """
    i = 0
    pos = -1
    for item in lista:
        if item == elemento:
            pos = i
            break
        else:
            i += 1
    return pos

#### 3
def busquedaMatriz(matriz, filas, columnas, elemento):
    """
    Busqueda de un elemento al recorrer una matriz de filas x columnas elementos
    Resultado: (fila, columna) donde se encuentra el elemento. (-1, -1) si no se encuentra.
    """
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == elemento:
                return f, c
    return -1, -1

#### 4
def contarMayoresMenores(lista, elemento):
    """
    Contar el total de elementos mayores y de elementos menores a un elemento dado.
    Resultado: total de elementos mayores y total de elementos menores a un elemento
    """
    mayores = 0
    menores = 0
    for item in lista:
        if item > elemento:
            mayores += 1
        if item < elemento:
            menores += 1
    return mayores, menores


#### 5
def contarTripletasSumaCero(lista):
    """
    Contar 3-tuplas <e1, e2, e3> de elementos en la lista tal que e1 + e2 + e3 sea igual a 0
    Resultado: total de 3-tuplas de elementos cuya suma es 0
    """
    contador = 0
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            for k in range(j+1, len(lista)):
                if lista[i]+lista[j]+lista[k] == 0:
                    contador += 1
    return contador



#### 6
def busquedaBinaria(listaOrdenada, elemento):
    """
    Busqueda Binaria de un elemento en una lista ordenada ascendentemente
    Resultado: Indice en la lista donde se encuentra el elemento. -1 si no se encuentra.
    """
    i = 0
    f = len(listaOrdenada) - 1
    pos = -1
    encontro = False
    while i <= f and not encontro:
        # calcular la posicion de la mitad entre i y f
        m = (i + f) // 2
        if listaOrdenada[m] == elemento:
            pos = m
            encontro = True
        elif listaOrdenada[m] > elemento:
            f = m - 1
        else:
            i = m + 1
    return pos


#### 7
def incognita( lista ):
    """
    Entender el algoritmo y decir que problema resuelve
    """
    i = 0
    j = len(lista) - 1
    while ( i < j ):
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
        i += 1
        j -= 1

