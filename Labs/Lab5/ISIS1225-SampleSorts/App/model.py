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
# TODO importar los algoritmos de ordenamiento necesarios para el laboratorio

# TODO importar el modulo de ordenamiento personalizado para el lab 5

assert cf

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores
y otra para géneros
"""

# algoritmos de ordenamiento, por defecto no se ha seleccionado ninguno
sort_algorithm = None


# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {"books": None,
               "authors": None,
               "tags": None,
               "book_tags": None}

    catalog["books"] = new_list() #LinkedList or ArrayList
    catalog["authors"] = new_list()
    catalog["tags"] = new_list()
    catalog["book_tags"] = new_list()

    # llave temporal para el submuestreo de datos
    catalog["booksublist"] = None

    return catalog


# Funciones para agregar informacion al catalogo

def addBook(catalog, book):
    # Se adiciona el libro a la lista de libros
    add_last(catalog["books"], book)
    # Se obtienen los autores del libro
    authors = book["authors"].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        addBookAuthor(catalog, author.strip(), book)
    return catalog


def addBookAuthor(catalog, authorname, book):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog["authors"]
    posauthor = is_present(authors, authorname)
    if posauthor > 0:
        author = get_element(authors, posauthor)
    else:
        author = newAuthor(authorname)
        add_last(authors, author)
    add_last(author["books"], book)
    return catalog


def addTag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag["tag_name"], tag["tag_id"])
    add_last(catalog["tags"], t)
    return catalog


def addBookTag(catalog, booktag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newBookTag(booktag["tag_id"], booktag["goodreads_book_id"])
    add_last(catalog["book_tags"], t)
    return catalog


# Funciones para creacion de datos

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {"name": "", "books": None,  "average_rating": 0}
    author["name"] = name
    author["books"] = new_list()
    return author


def newTag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {"name": "", "tag_id": ""}
    tag["name"] = name
    tag["tag_id"] = id
    return tag


def newBookTag(tag_id, book_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    booktag = {"tag_id": tag_id, "book_id": book_id}
    return booktag


# funciones de configuracion para los algoritmos de ordenamiento

def selectSortAlgorithm(algo_opt):
    """selectSortAlgorithm permite seleccionar el algoritmo de ordenamiento
    para la lista de pokemon.

    Args:
        algo_opt (int): opcion de algoritmo de ordenamiento, las opciones son:
            1: Selection Sort
            2: Insertion Sort
            3: Shell Sort
            4: Merge Sort
            5: Quick Sort
            6: Heap Sort
            7: Bogo Sort
            8: Custom Sort (timsort o bucketsort)

    Returns:
        list: sort_algorithm (sort) la instancia del ordenamiento y
        algo_msg (str) el texto que describe la configuracion del ordenamiento
    """
    # TODO completar el ordenamiento personalizado para el lab 5
    # TODO nuevo del lab 5
    # respuestas por defecto
    sort_algorithm = None
    algo_msg = None

    # selecciona el algoritmo de ordenamiento
    # opcion 1: Selection Sort
    if algo_opt == 1:
        sort_algorithm = ses
        algo_msg = "Seleccionó la configuración - Selection Sort"

    # opcion 2: Insertion Sort
    elif algo_opt == 2:
        sort_algorithm = ins
        algo_msg = "Seleccionó la configuración - Insertion Sort"

    # opcion 3: Shell Sort
    elif algo_opt == 3:
        sort_algorithm = shs
        algo_msg = "Seleccionó la configuración - Shell Sort"

    # opcion 4: Merge Sort
    elif algo_opt == 4:
        sort_algorithm = mes
        algo_msg = "Seleccionó la configuración - Merge Sort"

    # opcion 5: Quick Sort
    elif algo_opt == 5:
        sort_algorithm = qus
        algo_msg = "Seleccionó la configuración - Quick Sort"

    # opcion 6: Heap Sort
    elif algo_opt == 6:
        sort_algorithm = hes
        algo_msg = "Seleccionó la configuración - Heap Sort"

    # opcion 7: Bogo Sort
    elif algo_opt == 7:
        sort_algorithm = bos
        algo_msg = "Seleccionó la configuración - Bogo Sort"

    # opcion 6: Custom Sort: timsort o bucketsort
    # TODO completar el ordenamiento personalizado para el lab 5
    elif algo_opt == 8:
        sort_algorithm = cus
        algo_msg = "Seleccionó la configuración - Custom Sort (Tim, Patience)"
    # respuesta final: algoritmo de ordenamiento y texto de configuracion
    return sort_algorithm, algo_msg


def setBookSublist(catalog, size):
    """
    Crea una sublista de libros de tamaño size
    """
    # TODO nuevo del lab 5
    books = catalog["books"]
    catalog["booksublist"] = sub_list(books, 1, size)
    return catalog


# Funciones de consulta

def getBooksByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    posauthor = is_present(catalog["authors"], authorname)
    if posauthor > 0:
        author = get_element(catalog["authors"], posauthor)
        return author
    return None


def getBestBooks(catalog, number):
    """
    Retorna los mejores libros
    """
    books = catalog["books"]
    bestbooks = new_list()
    for cont in range(1, number+1):
        book = get_element(books, cont)
        add_last(bestbooks, book)
    return bestbooks


def countBooksByTag(catalog, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    tags = catalog["tags"]
    bookcount = 0
    pos = is_present(tags, tag)
    if pos > 0:
        tag_element = get_element(tags, pos)
        if tag_element is not None:
            pass
            #loop over all book tags in catalog["book_tags"]
            #count the book that have the same tag_element["tag_id"] and book_tag["tag_id"]            
    #return bookcount


def bookSize(catalog):
    return size(catalog["books"])


def authorSize(catalog):
    return size(catalog["authors"])


def tagSize(catalog):
    return size(catalog["tags"])


def bookTagSize(catalog):
    return size(catalog["book_tags"])


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpAuthors(authorname1, author):
    if authorname1.lower() == author["name"].lower():
        return 0
    elif authorname1.lower() > author["name"].lower():
        return 1
    return -1


def cmpTagNames(name, tag):
    if (name == tag["name"]):
        return 0
    elif (name > tag["name"]):
        return 1
    return -1


def cmpBooks(bookid1, book):
    if bookid1 == book["goodreads_book_id"]:
        return 0
    elif bookid1 > book["goodreads_book_id"]:
        return 1
    return -1


# funciones para comparar elementos dentro de algoritmos de ordenamientos

def evalRatings(book1, book2):
    # TODO modificar operador de comparacion del lab 5
    return (float(book1["average_rating"]) > float(book2["average_rating"]))


# Funciones de ordenamiento

def sortBooks(catalog):
    # TODO completar los cambios del return para el sort lab 5 (Parte 1).
    sorted_books = catalog["booksublist"]
    sort_algorithm.sort(sorted_books, evalRatings)
