import numpy as np
import time

def sort(mass):
    l = len(mass)
    factor = 1.247
    gapF = l/factor
    while gapF > 1:
        gap = round(gapF)
        for i in range(l-gap):
            if mass[i] > mass[i+gap]:
                mass[i], mass[i+gap] = mass[i+gap], mass[i]
        gapF = gapF/factor
    return mass


mass = np.random.randint(1, 1000000, size=1000000)
start_time = time.time()
sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)
