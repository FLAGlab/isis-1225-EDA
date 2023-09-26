import linkedlist_2_sol as List

"""
 Queues are implemented as lists, where enqueue adds to 
 the end of the list and dequeue removes the first element
 Must import the correct list implementation
"""
#O(1)
def new_queue():
    """
    Create an empty queue
    """
    return List.create_list()

#O(1)
def enqueue(queue, elem):
    """
    Add an element to the end of the queue
    """
    List.add(queue, elem)

#O(1)
def dequeue(queue):
    """
    Remove the first element from the front of the queue
    all elements move to the front one position
    """
    #queue['head'] = queue['head']['next']
    head = List.first(queue)
    second = List.second(queue)
    List.update_head(queue, head, second)
    return head['value']


#O(1)
def peek(queue):
    """
    Check the first element of the queue
    """
    return List.first(queue)

#O(1)
def is_empty(queue):
    """
    Verifies if the queue is empty
    """
    #return List.first_value(queue) == None 
    return List.size(queue) == 0

#O(1)
def size(queue):
    """
    returns the number of elements in the queue
    """
    List.size(queue)