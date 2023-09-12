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
  La definición recursiva de la lista esta dada por:
      - Una lista es la lista vacía. [] aka None
      - Un elemento agregado como prefijo de una lista. a | list 
  Los elementos se cuentan desde la posición 1.
"""

def empty_list():
    """
    Definición de la lista vacía
    """
    return None

def cons(element, list):
    """
    Agrega el elemento element, como el primer elemento de la lista list
    """
    return {'info': element, 'next': list}

def head(list):
    """
    Retorna el primer elemento de la lista dada 
    """
    return list['info']

def tail(list):
    """
    returnla la lista conformada desde el segundo elemento de list
    """
    return list['next']

