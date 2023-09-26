#### 2
def incognita(n):
    sum = 0
    while n > 0:
        sum += n
        n = n // 2
    return sum



 
def incognita2(n):
    sum = 0
    while n > 0:
        for i in range(n):
            sum += 1
        n = n // 2
    return sum





from time import time
t0 = time()
incognita(100000)
t1 = time()
print('function1 takes %f' %(t1-t0))
t2 = time()
incognita2(100000)
t3 = time()
print('function2 takes %f' %(t3-t2))
