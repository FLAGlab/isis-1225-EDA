#O(n^2)
def selection_sort(list):
    """
    """
    for i in range(len(list)):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
    return list



#API
l = [1, 25, 16, 12, 22, 0, 64, 42, 6]
l2 = selection_sort(l)
print(l2)        