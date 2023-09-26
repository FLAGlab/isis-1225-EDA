
def order(l):
    count = 0
    while not ordered(l):
        elem = Q.dequeue(l)
        first = Q.peek(l)
        if elem < first:
            l.append(elem)
            count += 2
        else:
            l.append(l.pop(0))
            l.append(elem)
            count += 4
    return count


def ordered(l):
    ordered = True
    for i in range(len(l)-1):
        elem1 = l[i]
        elem2 = l[i+1]
        if elem1 > elem2:
            ordered = False
    return ordered

q = [53, 34, 74, 73, 42, 97, 57]
print(q)
print(order(q))
print(q)