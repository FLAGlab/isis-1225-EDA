
def insertion_sort(list):
    i = 0
    while i < len(list):
        for j in range(i+1, 0, -1):
            if list[j] < list[j-1]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
        i += 1 


l = [1, 25, 16, 12, 22, 0, 64, 42, 6]
insertion_sort(l)
print(l)      