def change(items, target):
    val = [float('infinity')] * (target + 1)             # Хранит максималньое число монет для i суммы
    val[0] = 0                                           # Нулевую сумму не надо разменивать

    for current in range(1, target + 1):                 # для каждой суммы перебираем все монеты, обновляем значение
        for item in items:
            if item <= current:
                val[current] = min(val[current], val[current - item] + 1)

    if val[target] != float('infinity'):
        return val[target]
    else:
        return "Нельзя разменять"


print(change([2, 5, 10], 14))
print(change([1, 4, 6], 8))
print(change([7, 9], 12))
print(change([5, 10, 25], 50))
print(change([1, 2, 5, 10], 27))
