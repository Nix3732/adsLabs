import numpy as np
import time

def sort(mass):
    step = len(mass) // 3
    while step > 0:
        for i in range(step, len(mass)):
            j = i
            d = j - step
            while d >= 0 and mass[d] > mass[j]:
                mass[d], mass[j] = mass[j], mass[d]
                j = d
                d = j - step
        step //= 3

    return mass

mass = np.random.randint(1, 100000, size=100000)
start_time = time.time()
sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)