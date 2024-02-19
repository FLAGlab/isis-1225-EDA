
#O(n^2)
def insertion_sort(list):
    """
    """
    for i in range(len(list)):
        to_change = i
        for j in range(i-1, -1, -1):
            if list[to_change] < list[j]:
                temp = list[to_change]
                list[to_change] = list[j]
                list[j] = temp
                to_change = j

#API
l = [1, 25, 16, 12, 22, 0, 64, 42, 6]
insertion_sort(l)
print(l)      