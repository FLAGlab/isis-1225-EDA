"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
assert cf

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores
y otra para géneros
"""

# Construccion de modelos


def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    # TODO lab 6, agregar llave de "titles" para el indice de libros
    catalog = {'books': None,
               'bookIds': None,
               'authors': None,
               'tags': None,
               'tagIds': None,
               'years': None}

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['books'] = new_list() #LINKED-LIST

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador del libro
    """
    catalog['bookIds'] = new_map() #SIZE=10000, SEPARATE-CHAINING, loadfactor=4

    """
    Este indice crea un map cuya llave es el autor del libro
    """
    catalog['authors'] = new_map() #SIZE=800, SEPARATE-CHAINING, loadfactor=4
    """
    Este indice crea un map cuya llave es la etiqueta
    """
    catalog['tags'] = new_map()#SIZE=34500, LINEAR-PROBING, loadfactor=0.5

    """
    Este indice crea un map cuya llave es el Id de la etiqueta
    """
    catalog['tagIds'] = new_map()#SIZE=34500, LINEAR-PROBING, loadfactor=0.5

    """
    Este indice crea un map cuya llave es el año de publicacion
    """
    catalog['years'] = new_map()#SIZE=40, LINEAR-PROBING, loadfactor=0.5

    """
    Este indice crea un map cuya llave es el titulo del libro
    La columna 'titles' del archivo books.csv
    """
    # TODO lab 6, agregar el ADT map con newMap()
    catalog['titles'] = None

    return catalog


# Funciones para creacion de datos

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    author = {'name': "",
              "books": None,
              "average": 0,
              "average_rating": 0}
    author['name'] = name
    author['books'] = new_list() #LINKED-LIST
    return author


def newBookTag(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_books': 0,
           'books': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['books'] = new_list()
    return tag


# Funciones para agregar informacion al catalogo

def addBook(catalog, book):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    add_last(catalog['books'], book)
    put(catalog['bookIds'], book['goodreads_book_id'], book)
    authors = book['authors'].split(",")  # Se obtienen los autores
    for author in authors:
        addBookAuthor(catalog, author.strip(), book)
    addBookYear(catalog, book)


def addBookYear(catalog, book):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    try:
        years = catalog['years']
        if (book['original_publication_year'] != ''):
            pubyear = book['original_publication_year']
            pubyear = int(float(pubyear))
        else:
            pubyear = 2020
        existyear = contains(years, pubyear)
        if existyear:
            entry = get(years, pubyear)
            year = get_value(entry)
        else:
            year = newYear(pubyear)
            put(years, pubyear, year)
        add_last(year['books'], book)
    except Exception:
        return None


def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = new_list() #LINKED-LIST
    return entry


def addBookAuthor(catalog, authorname, book):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    authors = catalog['authors']
    existauthor = contains(authors, authorname)
    if existauthor:
        entry = get(authors, authorname)
        author = get_value(entry)
    else:
        author = newAuthor(authorname)
        put(authors, authorname, author)
    add_last(author['books'], book)
    author['average'] += float(book['average_rating'])
    totbooks = size(author['books'])
    if (totbooks > 0):
        author['average_rating'] = author['average'] / totbooks


def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo y se
    actualiza el indice de identificadores del tag.
    """
    newtag = newBookTag(tag['tag_name'], tag['tag_id'])
    put(catalog['tags'], tag['tag_name'], newtag)
    put(catalog['tagIds'], tag['tag_id'], newtag)


def addBookTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = get(catalog['tagIds'], tagid)

    if entry:
        tagbook = get(catalog['tags'], get_value(entry)['name'])
        tagbook['value']['total_books'] += 1
        tagbook['value']['count'] += int(tag['count'])
        book = get(catalog['bookIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['books'], book['value'])


def addBookTitle(catalog, book):
    # TODO lab 6, agregar el libro al map de titulos originales
    """
    Completar la descripcion de addBookTitle
    """
    pass


# ==============================
# Funciones de consulta
# ==============================


def getBooksByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = get(catalog['authors'], authorname)
    if author:
        return get_value(author)
    return None


def getBooksByTag(catalog, tagname):
    """
    Retornar la lista de libros asociados a un tag
    """
    tag = get(catalog['tags'], tagname)
    books = None
    if tag:
        books = get_value(tag)['books']
    return books


def getBooksByYear(catalog, year):
    """
    Retorna los libros publicados en un año
    """
    year = get(catalog['years'], year)
    if year:
        return get_value(year)['books']
    return None


def getBookByTitle(catalog, title):
    # TODO lab 6, retornar el libro con el titulo dado
    """
    Completar la descripcion de getBookByTitle
    """
    pass


def booksSize(catalog):
    """
    Número de libros en el catago
    """
    return size(catalog['books'])


def authorsSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return size(catalog['authors'])


def tagsSize(catalog):
    """
    Numero de tags en el catalogo
    """
    return size(catalog['tags'])


def titlesSize(catalog):
    # TODO lab 6, retornar el numero de libros en el catalogo
    """
    Completar la descripcion de titlesSize
    """
    pass


# ==============================
# Funciones de Comparacion
# ==============================


def compareBookIds(id1, id2):
    """
    Compara dos ids de dos libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareMapBookIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = get_key(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareAuthorsByName(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = get_key(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareTagNames(name, tag):
    tagentry = get_key(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1


def compareTagIds(id, tag):
    tagentry = get_key(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return -1


def compareMapYear(year, book):
    bookentry = get_key(book)
    if (year == bookentry):
        return 0
    elif (year > bookentry):
        return 1
    else:
        return -1


def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return -1


def compareTitles(title, book):
    # TODO lab 6, cmp para comparar dos titulos de libros para ADT Map
    """ Completar la descripcion de compareTitles

    Args:
        title (str): titulo del libro
        book (ADT mapentry): map entry con el libro

    Returns:
        int: retrona 0 si son iguales, 1 si el primero es mayor
        y -1 si el primero es menor
    """
    pass
