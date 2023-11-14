

def new_graph(n):
    '''Crear un grafo de n nodos'''
    pass

def vertices(graph):
    '''Retorna una lista con los nodos del grafo'''
    pass

def edges(graph):
    '''Retorna una lista de tuplas (u,v,c) con todos los ejes del grafo'''
    pass

def degree(graph, v):
    '''
    Retorna la cantidad de arcos incidentes en el grafo
    La dirección de los ejes no influye sobre el grado
    '''
    pass

def add_edge(graph, u, v, cost=1):
    '''
    Crea un arco entre el vertice u y el vertice v con costo c
    El costo por defecto de los arcos es 1
    '''
    pass

def num_vertices(graph):
    ''' Retorna la cantidad de nodos del grafo'''
    pass

def num_edges(graph):
    '''Retorna la cantidad de arcos del grafo'''


def insert_vertex(grpah, u):
    '''
    Inserta un vertice nuevo al grafo
    '''
    pass

def remove_vertex(graph, u):
    '''
    Elimina el vertice u del grafo
    '''
    pass

def get_edge(graph, u, v):
    '''
    Retorna una lista de los ejes existentes entre los nodos u y v, 
    como una tripla (u,v,c)
    '''
    pass

def adjacents(graph, u):
    '''Retorna la lista de todos los nodos adyacentes a u'''
    pass