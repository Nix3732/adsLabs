import numpy as np
import time

def sort(mass):
    for i in range(1, len(mass)):
        j = i

        while j > 0 and mass[j - 1] > mass[i]:
            mass[j] = mass[j - 1]
            j -= 1

        mass[j] = mass[i]

    return mass

mass = np.random.randint(1, 1000000, size=1000000)
start_time = time.time()
sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)