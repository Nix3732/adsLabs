import numpy as np
import time

def heap(mass, l, i):
    large = i
    lft = 2*i+1
    rgh = 2*i+2

    if lft < l and mass[i] < mass[lft]:
        large = lft
    if rgh < l and mass[large] < mass[rgh]:
        large = rgh
    if large != i:
        mass[i], mass[large] = mass[large], mass[i]
        heap(mass, l, large)

def sort(mass):
    l = len(mass)
    for i in range(l, -1, -1):
        heap(mass, l, i)
    for i in range(l-1, 0, -1):
        mass[i], mass[0] = mass[0], mass[i]
        heap(mass, i, 0)
    return mass


mass = np.random.randint(1, 100000, size=100000)
start_time = time.time()
mass =  sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)