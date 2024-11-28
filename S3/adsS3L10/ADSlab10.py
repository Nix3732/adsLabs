import numpy as np
import time

def sort(mass):
    if len(mass) == 0 or len(mass) == 1: # Если массив пустой или содержит один элемент, возвращаем его
        return mass
    m1 = sort(mass[:len(mass)//2]) # Делим массивы на одинаковые по длине
    m2 = sort(mass[len(mass)//2:])

    c = [0] * len(mass)
    m1count, m2count, ccount = 0, 0, 0

    while len(m1) > m1count and len(m2) > m2count: #Сравниваем элементы из обоих массивов
        if m1[m1count] <= m2[m2count]:
            c[ccount] = int(m1[m1count])
            m1count+=1
        else:
            c[ccount] = int(m2[m2count])
            m2count+=1
        ccount+=1

    while m1count < len(m1): #Добавляем оставшиеся элементы из обоих массивов
        c[ccount] = int(m1[m1count])
        m1count += 1
        ccount += 1
    while m2count < len(m2):
        c[ccount] = int(m2[m2count])
        m2count += 1
        ccount += 1
    return c


mass = np.random.randint(1, 100000, size=100)
start_time = time.time()
mass = sort(mass)
end_time = time.time()
print(end_time - start_time)
print(mass)