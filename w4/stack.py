
"""
 Stacks are implemented as lists, where push adds to 
 the head of the list and pop removes the first element
 You have to use the most convenient implementation of list
"""
#O(1)
def new_stack():
    """
    Create an empty stack with a pointer to its head
    keep the size of the stack as a structure variable
    """
    
#O(1)
def is_empty(s):
    """
    Verifies if the stack is empty
    """

#O(1)
def size(s):
    """
    returns the number of elements in the stack
    """    
#O(1)
def push(s, elem):
    """
    Add an element to the top of the stack
    """
    
#O(1)
def pop(s):
    """
    Remove the first element from the top of the stack
    all elements move to the front one position
    """
    
#O(1)
def top(s):
    """
    Check the first element in the top of the stack
    """
    
    
def main():
    s = new_stack()
    s = push(s, 4)
    s = push(s, 2)
    print(s)

main()