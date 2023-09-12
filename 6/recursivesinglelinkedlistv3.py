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
"""
  Este módulo implementa una estructura de datos lineal mediante una lista
  encadenada sencillamente RECURSIVA para almacenar una colección de elementos.
  Se definen los algoritmos recursivos que implementan su funcionalidad.
  La definición recursiva de la lista esta dada por:
      - Una lista es la lista vacía. [] aka None
      - Un elemento agregado como prefijo de una lista. a | list 
"""

def create_list():
    """
    Definición de la lista vacía
    """
    return None

def cons(list, elem):
    """
    Agrega el elemento element, como el primer elemento de la lista list
    """
    if list == None:
        return {'v': elem, 'next': None}
    else:
        return {'v':elem, 'next': list}

def head(list):
    """
    Retorna el primer elemento de la lista dada 
    """
    if list == None:
        return None
    else:
        return list['v']

def tail(list):
    """
    returnla la lista conformada desde el segundo elemento de list
    """    
    if list == None:
        return None
    else:
        return list['next']
    
def size(list):
    def size_iter(list, length):
        if list == None:
            return length
        else:
            return size_iter(tail(list), length + 1)
    size_iter(list, 0)

def is_present(list, elem):
    def is_present_iter(list, pos):
        if list == None:
            return -1
        elif head(list) == elem:
            return pos
        else:
            is_present_iter(tail(list), pos + 1)
    is_present_iter(list, 0)
