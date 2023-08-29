
#List implemantation with pointers to the first and last

head = {'value': None, 'next': None} 
last = head
size = 0

#O(1)
def add(new_elem):
    global size
    global last

    size += 1
    if head['value'] == None and head['next'] == None:
        head['value'] = new_elem
    else :
        elem = {'value': new_elem, 'next': None}
        last['next'] = elem
        last = elem
    
#O(n)
def delete(value):
    global size

    elem = head
    while elem['next']['value'] != value:
        elem = elem['next']
    elem['next'] = elem['next']['next']
    size = size - 1

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

#O(1)
def length():
    global size 

    return size







