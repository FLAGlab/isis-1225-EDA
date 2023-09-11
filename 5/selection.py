
def selection_sort(list):
    for ordered in range(len(list)):
        min = list[ordered]
        min_index = ordered
        for i in range(ordered, len(list)):
            if min > list[i]:
                min = list[i]
                min_index = i
        temp = list[ordered]
        list[ordered] = min
        list[min_index] = temp



l = [1, 25, 16, 12, 22, 0, 64, 42, 6]
selection_sort(l)
print(l)        