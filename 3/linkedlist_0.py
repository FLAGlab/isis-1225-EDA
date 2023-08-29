
#Simple list implementation

head = {'value': None, 'next': None} 

#O(n)
def add(new_elem):
    if head['value'] == None and head['next'] == None:
        head['value'] = new_elem
    else :
        elem = head
        while elem['next'] != None:
            elem = elem['next']
        elem['next'] = {'value': new_elem, 'next': None}
    
#O(n)
def delete(value):
    elem = head
    while elem['next']['value'] != value:
        elem = elem['next']
    elem['next'] = elem['next']['next']


#O(n)
def search(val):
    elem = head
    while elem['next'] != None:
        if elem['value'] == val:
            return elem['value']
        else:
            elem = elem['next']

#O(n)    
def update(val, new_val):
    elem = head
    while elem['next'] != None:
        if elem['value'] == val:
            elem['value'] = new_val
        else:
            elem = elem['next']

#O(n)
def length():
    elem = head
    size = 0
    while elem['next'] != None:
        size += 1
    return size






