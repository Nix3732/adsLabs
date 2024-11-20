import numpy as np
import time

def sort(mass):
    m = max([len(str(x)) for x in mass])
    base = 10
    bin = [[] for i in range(base)]
    for i in range(0, m):
        for j in mass:
            d = (j//(base**i))%base
            bin[d].append(j)
        mass = [int(g) for q in bin for g in q]
        bin = [[] for i in range(base)]
    return mass


mass = np.random.randint(1, 100000, size=100)
start_time = time.time()
mass = sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)