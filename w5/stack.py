"""
 Queues are implemented as lists, where push adds to 
 the start of the list and pop removes the first element
 Must import the correct list implementation
"""
#O(1)
def new_stack():
    """
    Create an empty stack
    """
    #return {'value': None, 'next': None}
    return List.new_list()

#O(1)
def push(stack, value):
    """
    Adds an element to the top of the stack
    """
    #elem - List.create_element()
    elem = {'value': value, 'next': None}
    elem['next'] = List.first(stack)
    List.change_head(stack, elem) #stack['head'] = elem

#O(1)
def pop(stack):
    """
    Removes the top element of the stack
    """
    second = List.second(stack)
    List.change_head(stack, second)

#O(1)
def top(stack):
    """
    Returns the top element of the stack without removing it
    """
    List.first(stack)

#O(1)
def is_empty():
    """
    Verifies if the stack is empty
    """
    return List.size() == 0
    #return List.first_value() == None

#O(1)
def size():
    """
    Returns the size of the stack
    """
    return List.size()