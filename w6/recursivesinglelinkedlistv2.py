"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Fernando De la Rosa
 *
 """

import config
# from DISClib.DataStructures import listnode as node
from DISClib.Utils import error as error
import csv
assert config

"""
  Este módulo implementa una estructura de datos lineal mediante una lista
  encadenada sencillamente RECURSIVA para almacenar una colección de elementos.
  Se definen los algoritmos recursivos que implementan su funcionalidad.
  Los elementos se cuentan desde la posición 1.

"""

def newList(element, cmpfunction, module, key, filename, delim):
    """Crea una lista con un elemento.

    Se inicializan los apuntadores a la primera en None.
    El tipo de la listase inicializa como SINGLE_LINKED
    Args:
        element: nuevo elemento que tendra la lista

        cmpfunction: Función de comparación para los elementos de la lista.
        Si no se provee una función de comparación, se utilizará la función
        de comparación por defecto pero se debe suministrar un valor para key

        key: Identificador que se debe utilizar para la comparación de
        elementos de la lista

        filename: Si se provee este valor, se creará una lista a partir de
        la informacion que se encuentra en el archivo CSV

        delimiter: Si se provee un archivo para crear la lista, indica el
        delimitador a usar para separar los campos del archivo CSV

    Returns:
        Un diccionario que representa la estructura de datos de una lista
        encadanada vacia (recursiva).

    Raises:

    """
    newlist = {'info': element,
               'next': None,     # conecta la sublista que le sigue
               'size': 1,
               'key': key,
               'type': 'SINGLE_LINKED',
               'datastructure': module
               }

    if cmpfunction is None:
        newlist['cmpfunction'] = defaultfunction
    else:
        newlist['cmpfunction'] = cmpfunction

    if filename is not None:
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=delim)
        for line in input_file:
            addLast(newlist, line)
    return newlist

def head(lst):
    """
    Retorna el valor del primer elemento de la lista
    """
    if lst == None:
        return None
    else:
        return lst['info']


def tail(lst):
    """
    Retorna la sublista que sigue a la lista de referencia
    Args:
        lst: lista de referencia para consultar su sublista
    """
    try:
        if lst is None:
            return None
        else:
            return lst['next']
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->tail: ')
    
#cons
def addFirst(lst, element):
    """Agrega una lista al inicio de la lista de referencia.

    Agrega una lista al principio, ajusta el apuntador
    al primer elemento e incrementa el tamaño de la lista.

    Args:
        lst:  La lista donde inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el proceso
        fue exitoso

    Raises:
        Exception
    """
    try:
        nuevaLista = newList(element, lst['cmpfunction'], lst['datastructure'], lst['key'], None, None)
        nuevaLista['next'] = lst
        nuevaLista['size'] = 1 + lst['size']
        return nuevaLista
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->addFirst: ')

#remove
def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista (algoritmo recursivo).

    Se adiciona un elemento en la última posición de la lista y se actualiza
     el apuntador a la útima posición.
    Se incrementa el tamaño de la lista en 1
    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        if lst is None:
            return newList(element, lst['cmpfunction'], lst['datastructure'], lst['key'], None, None)
        else:
            lst['next'] = addLast(tail(lst), element)        # aplicancion de Recursion a la sublista tail(lst) 
            lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->addLast: ')


def isEmpty(lst):
    """ Indica si la lista está vacía
    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst is None
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->isEmpty: ')


def size(lst):
    """ Informa el número de elementos de la lista (algoritmo recursivo).
    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if isEmpty(lst):
            return 0
        else:
            return 1 + size(tail(lst))             # aplicancion de Recursion a la sublista tail(lst)
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->size: ')

def isPresent(lst, element):
    """
    Buscar si el elemento esta presenta en la lista.
    Informa si un elemento está en la lista.  Si esta presente,
    retorna la posición en la que se encuentra  o cero (0) si no esta presente.

    Args:
        lst: lista de busqueda
        element:_ elemento de busqueda
    """
    try:
        if lst is None:
            return 0
        elif lst['cmpfunction'](lst['info'], element) == 0:
            return 1
        else:
            pos_Sublista = isPresent(tail(lst), element)    # aplicancion de Recursion a la sublista tail(lst)
            if pos_Sublista != 0:
                return 1 + pos_Sublista
            else:
                return 0
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist:isPresentNode')


# _____________________________________________________________________
#            Funciones Helper
# _____________________________________________________________________

def defaultfunction(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1
