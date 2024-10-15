import sys
import math

x = str(input("Введите целое число:\n"))
answer = []

if not x.isdigit():
    print("Вы ввели не число")
    sys.exit()
else:
    x = int(x)
    power = int(math.log(x, 3)+1)
    for k in range(power + 1):
        for l in range(power + 1 - k):
            for m in range(power + 1 - k - l):
                num = 3**k * 5**l * 7**m
                if num <= x and num not in answer:
                    answer.append([num, k, l, m])
answer.sort()
print('x', 'k', 'l', 'm')
for i in answer:
    print(*i)

