import numpy as np
import time

def sort(mass):
    for i in range(len(mass)-1):
        i_min = i
        for j in range(i+1, len(mass)):
            if mass[j] < mass[i_min]:
                mass[i], mass[j] = mass[j], mass[i]

    return mass


mass = np.random.randint(1, 100000, size=100000)
start_time = time.time()
mass = sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)
