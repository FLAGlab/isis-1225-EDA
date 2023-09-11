
def shell_sort(list):
    N = len(list)
    h = 1
    while h < N/3:
        h = int(3*h + 1)
        while h >= 1:
            for i in range(h, N):
                j = i
                while j >=h and list[j+1] < list[j-h+1]:
                    temp = list[j+1]
                    list[j+1] = list[j-h+1]
                    list[j-h+1] = temp
                    j -=h
            h //= 3

l = [1, 25, 16, 12, 22, 0, 64, 42, 6]
shell_sort(l)
print(l) 