
agenda = []

def agregar_contacto(nom, tel):
    id = len(agenda)
    contacto = (id, nom, tel)
    agenda.append(contacto)

def buscar_contacto(nom):
    c = ()
    for contacto in agenda:
        if contacto[1] == nom:
            c = contacto
    return c

def buscar_contacto(tel):
    c = ()
    for contacto in agenda:
        if contacto[2] == tel:
            c = contacto
    return c

def borrar_contacto(tel):
    contacto = buscar_contacto(tel)
    
