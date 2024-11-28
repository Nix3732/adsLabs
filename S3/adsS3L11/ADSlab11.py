import numpy as np
import time

def sort(mass):
    if len(mass) <= 1:
        return mass

    p = mass[np.random.randint(0, len(mass))]
    l = [int(x) for x in mass if x < p]
    m = [int(x) for x in mass if x == p]
    r = [int(x) for x in mass if x > p]
    return sort(l) + m + sort(r)

mass = np.random.randint(1, 100000, size=10000)
start_time = time.time()
mass = sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)