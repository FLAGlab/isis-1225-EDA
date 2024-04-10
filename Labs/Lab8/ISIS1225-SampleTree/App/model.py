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
 """
import config
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros.

Los autores, los tags y los años se guardaran en
tablas de simbolos.
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'crimes': None,
                'dateIndex': None
                }

    analyzer['crimes'] = None #lt.new_list()
    analyzer['dateIndex'] = None #new_bst compare by dates
    return analyzer


# Funciones para agregar informacion al catalogo


def addCrime(analyzer, crime):
    """
    funcion que agrega un crimen al catalogo
    """
    add(analyzer['crimes'], crime)
    updateDateIndex(analyzer['dateIndex'], crime)
    return analyzer


def updateDateIndex(map, crime):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = crime['OCCURRED_ON_DATE']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = get(map, crimedate.date()) #TODO
    if entry is None:
        datentry = newDataEntry(crime)
        add(map, crimedate.date(), datentry) #TODO
    else:
        datentry = getValue(entry) #TODO
    addDateIndex(datentry, crime)
    return map


def addDateIndex(datentry, crime):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstcrimes']
    add(lst, crime) #TODO
    offenseIndex = datentry['offenseIndex']
    offentry = get(offenseIndex, crime['OFFENSE_CODE_GROUP']) #TODO
    if (offentry is None):
        entry = newOffenseEntry(crime['OFFENSE_CODE_GROUP'], crime)
        addLast(entry['lstoffenses'], crime) #TODO
        put(offenseIndex, crime['OFFENSE_CODE_GROUP'], entry) #TODO
    else:
        entry = get_value(offentry) #TODO
        add(entry['lstoffenses'], crime) #TODO
    return datentry


def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = []#hash_table_linear_probing(numelements=30)
    entry['lstcrimes'] = new_list() #TODO
    return entry


def newOffenseEntry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = new_list()
    return ofentry


# ==============================
# Funciones de consulta
# ==============================


def crimesSize(analyzer):
    """
    Número de crimenes
    """
    return size(analyzer['crimes']) #TODO


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return height(analyzer['dateIndex']) #TODO


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return size(analyzer['dateIndex']) #TODO


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return minKey(analyzer['dateIndex']) #TODO


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return maxKey(analyzer['dateIndex']) #TODO


def getCrimesByRange(analyzer, initialDate, finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    lst = values(analyzer['dateIndex'], initialDate, finalDate) #TODO
    totcrimes = 0
    for lstdate in iterator(lst): #TODO
        totcrimes += size(lstdate['lstcrimes']) #TODO
    return totcrimes


def getCrimesByRangeCode(analyzer, initialDate, offensecode):
    """
    Para una fecha determinada, retorna el numero de crimenes
    de un tipo especifico.
    """
    crimedate = get(analyzer['dateIndex'], initialDate) #TODO
    if crimedate['key'] is not None:
        offensemap = getValue(crimedate)['offenseIndex'] #TODO
        numoffenses = get(offensemap, offensecode) #TODO
        if numoffenses is not None:
            return size(get_value(numoffenses)['lstoffenses']) #TODO
    return 0


# ==============================
# Funciones de Comparacion
# ==============================


def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareOffenses(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    offense = get_key(offense2) #TODO
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1
